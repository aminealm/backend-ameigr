from django.db import models
from django.contrib.auth.models import User

class Bureau(models.Model):
    name = models.CharField(max_length=100)
    Text = models.CharField(max_length=100)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Specify a default value
    Image = models.ImageField(upload_to='api/images/', null=False, default='default_image.jpg')
    link = models.URLField(default='https://example.com')
    link2 = models.URLField(default='https://example.com')



