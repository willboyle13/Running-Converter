from django.db import models

# Create your models here.

class AdvancedCalc(models.Model):
    events = models.CharField(max_length=100)
    time = models.CharField(max_length=100)