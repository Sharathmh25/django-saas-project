from django.db import models

from account.models import User
from tenant.models import Tenant
CHOICES=[
    ('Pending','PENDING'),
    ('Done','DONE')
]
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField()
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=225,choices=CHOICES,default='Pending')