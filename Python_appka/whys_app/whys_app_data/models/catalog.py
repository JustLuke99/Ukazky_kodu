from django.db import models
from .image import Image
from .product import Product
from .attribute import Attribute

class Catalog(models.Model):
    nazev = models.CharField(default= None, null=True, max_length=100)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    
    products_ids = models.ManyToManyField(Product)
    attributes_ids = models.ManyToManyField(Attribute)
