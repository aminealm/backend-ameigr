from django.shortcuts import render
from .models import Comite
from .serializers import PostSerializer
from rest_framework import generics,permissions, mixins,status

# Create your views here.

class PostComite(generics.ListCreateAPIView):
    queryset = Comite.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

