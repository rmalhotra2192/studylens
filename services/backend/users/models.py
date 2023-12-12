from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class Learner(AbstractUser):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    is_test_user = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=250, default="John", blank=True)
    last_name = models.CharField(max_length=250, default="Doe", blank=True)
    email = models.CharField(max_length=500, unique=True, null=False, blank=False)

    groups = models.ManyToManyField(Group, related_name="learner_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="learner_permissions"
    )


class Moderator(AbstractUser):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    is_active = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=250, default="John", blank=True)
    last_name = models.CharField(max_length=250, default="Doe", blank=True)
    email = models.CharField(max_length=500, unique=True, null=False, blank=False)

    groups = models.ManyToManyField(Group, related_name="moderator_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="moderator_permissions"
    )
