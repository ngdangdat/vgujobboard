# Generated by Django 2.0.3 on 2018-08-19 16:08

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_onetimepassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='job_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='major_intake',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='message',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='office',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='profile_pics/%Y-%m-%d/', validators=[core.validators.validate_avatar], verbose_name='Profile avatar'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='profile',
            name='intake',
            field=models.PositiveSmallIntegerField(default=2008, validators=[core.validators.validate_intake], verbose_name='Intake'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile URL'),
        ),
        migrations.AddField(
            model_name='profile',
            name='major',
            field=models.PositiveSmallIntegerField(choices=[(3, 'EEIT'), (5, 'FA')], default=1, verbose_name='Major'),
        ),
        migrations.AddField(
            model_name='profile',
            name='organization',
            field=models.CharField(default='', max_length=255, verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Male'), (3, 'Female'), (5, 'Undefined')], default=5, verbose_name='Gender'),
        ),
    ]
