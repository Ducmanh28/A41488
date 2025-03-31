from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)