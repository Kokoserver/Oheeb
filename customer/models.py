from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, auth

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.subject
    
    
