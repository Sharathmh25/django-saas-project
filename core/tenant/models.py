from django.db import models

# Create your models here.
class Tenant(models.Model):
    name=models.CharField(max_length=225)
    domain=models.CharField(max_length=225,unique=True)
    created_at=models.DateTimeField(auto_now=True)