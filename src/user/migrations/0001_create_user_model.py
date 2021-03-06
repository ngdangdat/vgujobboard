# Generated by Django 2.0.3 on 2018-08-31 17:02

import core.validators
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designate if user can log in admin site', verbose_name='Staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.', verbose_name='Active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(blank=True, default=None, error_messages={'unique': 'A user with that email already exists.'}, help_text='Required field.', max_length=245, null=True, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
            ],
            options={
                'db_table': 'auth_user',
                'permissions': (),
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(db_index=True, max_length=32)),
                ('send_counter', models.PositiveIntegerField(default=0)),
                ('last_send', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_counter', models.PositiveIntegerField(default=0)),
                ('last_check', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (3, 'Female'), (5, 'Undefined')], default=5, verbose_name='Gender')),
                ('birthday', models.DateField(blank=True, default=None, null=True, verbose_name='Birthday')),
                ('avatar', models.ImageField(blank=True, max_length=255, null=True, upload_to='avatars/', validators=[core.validators.validate_avatar], verbose_name='Profile avatar')),
                ('major', models.PositiveSmallIntegerField(choices=[(3, 'EEIT'), (5, 'FA')], default=1, verbose_name='Major')),
                ('intake', models.PositiveSmallIntegerField(default=2008, validators=[core.validators.validate_intake], verbose_name='Intake')),
                ('phone_number', models.CharField(blank=True, default=None, max_length=15, null=True, validators=[core.validators.validate_phone_number], verbose_name='Phone Number')),
                ('state', models.CharField(default='', max_length=255, verbose_name='City of Residence')),
                ('country', models.CharField(default='', max_length=255, verbose_name='Country of Residence')),
                ('organization', models.CharField(default='', max_length=255, verbose_name='Organization')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Position/Major')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile URL')),
                ('status', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='onetimepassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otp_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
