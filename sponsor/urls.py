from django.urls import path,include
from . import views

app_name = 'sponsor'

urlpatterns = [
    path('', views.PostSponsor.as_view()) ,

] 

