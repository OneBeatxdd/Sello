from django.db import models
from django.urls import reverse


class Task(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.TextField(max_length=10000)
    Status = models.CharField(max_length=7, default='New')
    # To-Do Doing Completed QA Closed New

    def get_absolute_url(self):
        return reverse('view_task:index')

    def __str__(self):
        return self.Title
