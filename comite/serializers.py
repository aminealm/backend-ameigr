from rest_framework import serializers
from .models import Comite

class PostSerializer(serializers.ModelSerializer):
   
    class Meta : 
        model = Comite
        fields = ['id','name','vice_name','text','vice_text','Image_Chef','Image_Vicechef' , 'Image_Comité','link0','link1','link2','link3']


