from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
        
class usuario(DateTimeModel):
    id= models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)