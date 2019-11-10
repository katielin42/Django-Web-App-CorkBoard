from django.db import models
from django import forms
import datetime

# Create your models here.
class Poster(models.Model):
    eventName = models.CharField(max_length = 50)
    description = models.TextField()
    group = models.CharField(max_length=50)
    location = models.CharField(max_length = 50)
    date = models.DateField(default =datetime.date.today)
    time_start = models.TimeField(default = "10:00" )
    time_end = models.TimeField(default="3:00")
    poster = models.ImageField(default = "media/default_poster.jpg")
    category_tag = models.CharField(max_length = 50) #make radio buttons
    #Food Sale, Social Event, Classes, Talks, Activity
    #selected = models.BooleanField(default=False)

class CategoryModel(models.Model):
    category_selection= forms.CharField(label="Categories")
    field1 = forms.ChoiceField(widget=forms.RadioSelect)







