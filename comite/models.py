from django.db import models
from django.contrib.auth.models import User

class Comite(models.Model):
    name = models.CharField(max_length=100)
    vice_name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    vice_text = models.CharField(max_length=100)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Specify a default value
    Image_Chef = models.ImageField(upload_to='api/images/', null=False)
    Image_Vicechef = models.ImageField(upload_to='api/images/', null=False)
    Image_Comité = models.ImageField(upload_to='api/images/', null=False)
    link0 = models.URLField(default='https://facebook.com')
    link1 = models.URLField(default='https://instagram.com')
    link2 = models.URLField(default='https://facebook.com')
    link3 = models.URLField(default='https://instagram.com')



