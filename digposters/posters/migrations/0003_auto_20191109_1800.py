# Generated by Django 2.2.7 on 2019-11-10 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_auto_20191109_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='poster',
            name='category_tag',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poster',
            name='group',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poster',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poster',
            name='time_end',
            field=models.TimeField(default='3:00'),
        ),
    ]