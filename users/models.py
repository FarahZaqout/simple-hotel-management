from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  username = models.CharField(
    max_length=200,
    unique = True
    )
  email = models.EmailField(
    verbose_name = 'email address',
    max_length = 200,
    unique = True
  )

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ('email', 'password', 'first_name', 'last_name')

  def __str__(self):
    return self.username
