from rest_framework import serializers
from .models import Sponsor

class PostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Sponsor
        fields = ['id', 'Image']


