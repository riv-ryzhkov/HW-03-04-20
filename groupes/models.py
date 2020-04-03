from django.db import models

class Groupe(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    head = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, default='')
