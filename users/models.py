from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  username = models.CharField(max_length=200)
  email = models.EmailField(
    verbose_name = 'email address',
    max_length = 200,
    unique = True
  )

  def __str__(self):
    return self.username
