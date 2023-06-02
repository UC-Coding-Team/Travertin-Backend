from django.db import models

from core.utils.models import AbstractLayer


class Category(AbstractLayer):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
