from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length = 100)
    user = models.OneToOneField(get_user_model(),on_delete = models.CASCADE)