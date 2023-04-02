from django.db import models
from .product import Product
from .image import Image

class ProductImage(models.Model):
    nazev = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
