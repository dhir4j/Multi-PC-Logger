# pclogger/models.py
from django.db import models

class PC(models.Model):
    os = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    ram = models.FloatField()
    hdd = models.FloatField()
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
