from django.db import models

# Create your models here.
from django.db import models


class student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Store_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)

# Create your models here.
