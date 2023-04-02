from django.db import models

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=100)
