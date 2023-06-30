from rest_framework import serializers
from .models import Home

class PostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Home
        fields = ['id', 'Image']


