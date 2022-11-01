from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Dreamreal(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    pid = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    passwd = models.CharField(max_length=50)

    class Meta:
        db_table = 'dreamreal'
