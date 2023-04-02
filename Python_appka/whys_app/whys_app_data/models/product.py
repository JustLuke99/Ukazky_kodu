from django.db import models

class Product(models.Model):
    nazev = models.CharField(default= None, null=True, max_length=255)
    description = models.TextField(default= None, null=True)
    cena = models.CharField(default= None, null=True, max_length=20)
    mena = models.CharField(default= None, null=True, max_length=10)
    published_on = models.DateTimeField(default= None, null=True)
    is_published = models.BooleanField(default= None, null=True)