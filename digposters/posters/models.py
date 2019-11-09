from django.db import models

# Create your models here.
class Poster(models.Model):
    eventName = models.CharField(max_length = 50)
    description = models.TextFiled(max_length = 150)


