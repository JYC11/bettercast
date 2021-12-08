from django.db import models

# Create your models here.

class Test(models.models):
    name = models.CharField(max=250)
    colour = models.CharField(max=250)
    link = models.CharField(max=250)