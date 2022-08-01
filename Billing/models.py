from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.TextField(max_length=200)
    subcategory = models.TextField(max_length=200)
    updated_on = models.TimeField(auto_now_add=True, blank=True)
    created_on = models.TimeField(auto_now=True, blank=True)
