from django.db import models
from .attribute import Attribute
from .product import Product

class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)