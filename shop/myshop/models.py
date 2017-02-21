from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=50)
    item_image= models.ImageField(upload_to='images/', default='images/ipad.jpg')
    price=models.IntegerField()
    item_description=models.CharField(max_length=50)
    item_stock=models.IntegerField()


    def __str__(self):
        return self.item_name