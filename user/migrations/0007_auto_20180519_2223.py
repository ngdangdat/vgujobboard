# Generated by Django 2.0.3 on 2018-05-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180519_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='message',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Message to VGU Alumni Community'),
        ),
    ]
