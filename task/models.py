from django.db import models
from django.urls import reverse


class Task(models.Model):
    STATUS_CHOICES = [
        ('To-Do', 'To-Do'),
        ('Doing', 'Doing'),
        ('Completed', 'Completed'),
        ('QA', 'QA'),
        ('Closed', 'Closed'),
        ('New', 'New')
    ]

    # the fields
    Title = models.CharField(max_length=250)
    Description = models.TextField(max_length=10000)
    Status = models.CharField(max_length=7,
                              default='New',
                              choices=STATUS_CHOICES,)
    # To-Do Doing Completed QA Closed New

    def get_absolute_url(self):
        return reverse('task:index')

    def __str__(self):
        return self.Title
