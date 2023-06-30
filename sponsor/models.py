from django.db import models
from django.contrib.auth.models import User

class Sponsor(models.Model):
    Image = models.ImageField(upload_to='spnsor/images/', null=False)



