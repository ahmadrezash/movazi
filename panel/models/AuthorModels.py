from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    gender      = models.BooleanField() # True is man
    birth_date  = models.DateTimeField()
    avatar      = models.ImageField(upload_to='image/profile', max_length=None)
    last_update = models.DateTimeField()

