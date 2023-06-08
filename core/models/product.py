from django.db import models

from core.models.category import Category
from core.utils.models import AbstractLayer


class Product(AbstractLayer):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    slug = models.SlugField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
