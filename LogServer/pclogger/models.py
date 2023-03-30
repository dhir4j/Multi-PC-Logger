# File name: pclogger/models.py
from django.db import models

class PC(models.Model):
    pc_name = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    ram = models.FloatField()
    hdd = models.FloatField()
    ip_address = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pc_name
