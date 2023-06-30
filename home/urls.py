from django.urls import path,include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.PostHome.as_view()) ,

] 

