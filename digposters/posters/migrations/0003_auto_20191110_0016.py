# Generated by Django 2.2.7 on 2019-11-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.CharField(default='EE Club', max_length=50),
        ),
    ]
