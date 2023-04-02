from django.db import models
from .attributeName import AttributeName
from .attributeValue import AttributeValue

class Attribute(models.Model):
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.SET_NULL, null=True)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.SET_NULL, null=True)
