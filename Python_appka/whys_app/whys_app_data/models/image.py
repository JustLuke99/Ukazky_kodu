from django.db import models

class Image(models.Model):
    nazev = models.CharField(max_length=255, null=True)
    obrazek = models.TextField()
