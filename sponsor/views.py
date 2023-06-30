from django.shortcuts import render

from rest_framework import generics
from .models import Sponsor
from .serializers import PostSerializer


class PostSponsor(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


