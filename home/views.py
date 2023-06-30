from django.shortcuts import render

from rest_framework import generics
from .models import Home
from .serializers import PostSerializer


class PostHome(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


