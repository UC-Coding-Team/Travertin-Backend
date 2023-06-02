from django.db import models
from core.utils.models import AbstractLayer


class Discount(AbstractLayer):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField()

    def __str__(self):
        return self.title