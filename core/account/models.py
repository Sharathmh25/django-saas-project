from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from  tenant.models import Tenant
class User( AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE,blank=True,null=True)
