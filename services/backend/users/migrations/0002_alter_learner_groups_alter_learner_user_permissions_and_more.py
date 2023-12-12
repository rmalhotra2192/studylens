# Generated by Django 4.2.6 on 2023-12-09 22:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="learner",
            name="groups",
            field=models.ManyToManyField(
                related_name="learner_groups", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="learner",
            name="user_permissions",
            field=models.ManyToManyField(
                related_name="learner_permissions", to="auth.permission"
            ),
        ),
        migrations.CreateModel(
            name="Moderator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("is_active", models.BooleanField(blank=True, default=False)),
                (
                    "first_name",
                    models.CharField(blank=True, default="John", max_length=250),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, default="Doe", max_length=250),
                ),
                ("email", models.CharField(max_length=500, unique=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        related_name="moderator_groups", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        related_name="moderator_permissions", to="auth.permission"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
