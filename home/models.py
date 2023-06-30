from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    Image = models.ImageField(upload_to='home/images/', null=False)



