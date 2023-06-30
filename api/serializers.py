from rest_framework import serializers
from .models import Bureau

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    class Meta : 
        model = Bureau
        fields = ['id','name','Text','poster','poster_id','link','link2' , 'Image']


