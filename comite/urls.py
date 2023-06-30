from django.urls import path,include
from . import views

app_name = 'comite'

urlpatterns = [
    path('', views.PostComite.as_view()) ,

] 

