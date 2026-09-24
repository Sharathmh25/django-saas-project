from rest_framework import serializers
from .models import Task
class TaskSerilaizer(serializers.ModelSerializer):
        model=Task
        fields = ['title', 'description','status']
       