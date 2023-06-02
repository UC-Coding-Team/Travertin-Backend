from core.utils.models import AbstractLayer
from django.db import models



class Navbartex(AbstractLayer):
    STATUS_CHOICES = (
        ('green', 'Green'),
        ('red', 'Red'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='green')
    text = models.TextField()