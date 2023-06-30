from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from rest_framework import generics,permissions, mixins,status
from .models import Bureau
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Bureau.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class PostRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Bureau.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def delete(self,request,*args,**kwargs):
        post = Bureau.objects.filter(pk=kwargs['pk'],poster=self.request.user)
        if post.exists():
            return self.destroy(request,*args,**kwargs)
        else :
            raise ValidationError('This isn t ur post to delete')