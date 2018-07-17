from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.manager import Manager
from django.conf import settings
import facebook
import datetime


class JobFieldManager(Manager):
    pass


class JobField(models.Model):
    name = models.CharField(_('Field Name'), max_length=255, unique=True, null=True, blank=True)
    slug = models.SlugField()
    file_img_url = models.URLField(_('Image URL'), null=True, blank=True)
    
    objects = JobFieldManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(JobField, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Job(models.Model):
    field = models.ForeignKey(JobField, verbose_name=_('Job Field'),
                            related_name='field', null=True, on_delete=models.SET_NULL)
    other_field = models.CharField(_('Other Field'), null=True, blank=True, max_length=255)
    title = models.CharField(_('Job Title'), null=True, blank=True, max_length=255)
    company = models.CharField(_('Company'), null=True, blank=True, max_length=255)
    description = models.TextField(_('Job Description'), null=True, blank=True, max_length=255)
    requirement = models.TextField(_('Job Requirement'), null=True, blank=True, max_length=255)
    salary = models.CharField(_('Salary'), null=True, blank=True, max_length=255)
    benefit = models.TextField(_('Benefits'), null=True, blank=True, max_length=255)
    apply_contact = models.CharField(_('Resume Application To'), null=True, blank=True, max_length=255)
    deadline = models.DateField(_('Deadline'), null=True, blank=True)
    question_contact = models.CharField(_('For More Information'), null=True, blank=True, max_length=255)
    img_url = models.URLField(_('Image'), null=True, blank=True)
    is_posted = models.BooleanField(_('Posted'), default=False)
    scheduled_time = models.DateTimeField(_('Post scheduled time'), null=True, blank=True)
    facebook_post_id = models.CharField(_('Facebook Post ID'), null=True, blank=True, max_length=100)

    def __str__(self):
        return self.title

    @property
    def job_caption(self):
        fields = ['field', 'title', 'company', 'description', 'requirement', 'salary',
                'benefit', 'apply_contact', 'deadline', 'question_contact']
        meta = self._meta
        caption = ''
        for field in fields:
            section = None
            val = getattr(self, field, '')
            heading = meta.get_field(field).verbose_name
            if val:
                section = '[%s]\n%s' % (heading, val)
            elif field == 'field':
                section = '[%s]\n%s' % (heading, self.other_field)
            if section:
                caption = '%s\n\n%s' % (caption, section)
        return caption

    @property
    def job_image(self):
        if self.img_url:
            return self.img_url
        elif self.field and self.field.file_img_url:
            return self.field.file_img_url
        else:
            return settings.OTHER_JOB_IMAGE

    def save(self):
        self.post_to_facebook()
        super(Job, self).save()

    def get_schedule_time(self):
        '''
        Format:
            Mon 0
            Tue 1
            ...
            Sun 6
            (weekday, hour, minute)
        TODO Update schedule config using model
        TODO separate post_to_facebook and get_schedule_time
        '''
        scheduled_config = [
            (1, 12, 00),
            (5, 20, 50),
        ]

        if not scheduled_config:
            return None

        time_now = datetime.datetime.now()
        getNextWeekday = lambda date, day: date + datetime.timedelta(days=(day-date.weekday()+7)%7)
        scheduled_dates = []


        for (weekday, hour, minute) in scheduled_config:
            date = getNextWeekday(time_now, weekday).replace(
                hour=hour,
                minute=minute,
                second=0,
                microsecond=0
            )
            scheduled_dates.append(date)

        sorted_scheduled_dates = sorted(scheduled_dates)
        scheduled_time = None
        for date in sorted_scheduled_dates:
            delta_date = date - time_now
            if delta_date > datetime.timedelta(hours=4):
                scheduled_time = date
                break

        if not scheduled_time:
            scheduled_time = sorted_scheduled_dates[0] + datetime.timedelta(days=7)

        return scheduled_time

    def post_to_facebook(self):
        access_token = settings.FACEBOOK_ACCESS_TOKEN
        album_id = settings.FACEBOOK_ALBUM_ID
        poster = facebook.GraphAPI(access_token=access_token, version="2.10")
        params = dict()
        params['url'] = self.job_image
        params['caption'] = self.job_caption
        
        scheduled_time = self.get_schedule_time()
        if not scheduled_time:
            params['published'] = True
        else:
            params['published'] = False
            params['scheduled_publish_time'] = int(scheduled_time.timestamp())
            self.scheduled_time = scheduled_time

        path = '/%s/photos' % album_id
        try:
            result = poster.request(path=path, post_args=params, method='POST')
            if 'id' in result:
                self.facebook_post_id = result['id']
                self.is_posted = True
        except Exception:
            pass
