from django.contrib.auth.models import AbstractUser
from django.db import models

class Learner(AbstractUser):
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_test_user = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=250, default="John", blank=True)
    last_name = models.CharField(max_length=250, default="Doe", blank=True)
    email = models.CharField(max_length=500,unique=True, null=False, blank=False)
    