from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posterpics/')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ####stuff to delete if ur shit stops working.
    group = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField()  # default = django.utils.timezone.now
    time_start = models.TimeField(default="10:00")
    time_end = models.TimeField(default="3:00")
    category_tag = models.CharField(max_length=50)  # make radio buttons


    def __str__(self):
         return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
