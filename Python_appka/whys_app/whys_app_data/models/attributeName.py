from django.db import models

class AttributeName(models.Model):
    nazev = models.CharField(default= None, null=True, max_length=100)
    kod = models.CharField(default= None, null=True, max_length=30)
    zobrazit = models.BooleanField(default= None, null=True)
