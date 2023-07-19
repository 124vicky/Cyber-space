from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=12)
	gender = models.CharField(max_length=10)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']