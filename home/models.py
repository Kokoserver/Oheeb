from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.db.models import CASCADE

# Create your models here.
    
class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    image = models.FileField(upload_to='products')
    date = models.DateTimeField(default=datetime.now(), blank=True)
    category = models.CharField(max_length=20, default='general')
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    is_owned = models.BooleanField(default=False)
    user = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='pending')
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.user
    
