# Generated by Django 2.2.7 on 2019-11-09 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='category_tag',
            field=models.CharField(default='Social', max_length=50),
        ),
        migrations.AddField(
            model_name='poster',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='poster',
            name='group',
            field=models.CharField(default='University of Alberta', max_length=50),
        ),
        migrations.AddField(
            model_name='poster',
            name='location',
            field=models.CharField(default='Quad', max_length=50),
        ),
        migrations.AddField(
            model_name='poster',
            name='poster',
            field=models.ImageField(default='media/default_poster.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='poster',
            name='time_end',
            field=models.TimeField(default='15:00'),
        ),
        migrations.AddField(
            model_name='poster',
            name='time_start',
            field=models.TimeField(default='10:00'),
        ),
    ]
