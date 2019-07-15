from django.db import models

# Create your models here.

class ips(models.Model):
    num = models.CharField(max_length=150)
    ip = models.CharField(max_length=100)
    count = models.IntegerField(default=0)