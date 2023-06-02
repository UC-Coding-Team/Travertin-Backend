from core.utils.models import AbstractLayer
from django.db import models



class Navbartex(models.Model):
    STATUS_CHOICES = (
        ('green', 'Green'),
        ('red', 'Red'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='green')
    text = models.TextField()
    start_time = models.TimeField(default='09:00')
    end_time = models.TimeField(default='18:00')

    def __str__(self):
        return self.text