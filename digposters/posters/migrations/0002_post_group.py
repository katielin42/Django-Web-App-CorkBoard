# Generated by Django 2.2.7 on 2019-11-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.CharField(default='group', max_length=50),
            preserve_default=False,
        ),
    ]
