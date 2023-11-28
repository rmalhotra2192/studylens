# Generated by Django 4.2.6 on 2023-11-20 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resource",
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
                ("title", models.CharField(max_length=128)),
                ("cover", models.CharField(max_length=512, null=True)),
                ("description", models.TextField(null=True)),
                ("active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("difficulty", models.IntegerField(null=True)),
                ("last_review_status", models.CharField(max_length=128, null=True)),
                ("last_review_by", models.CharField(max_length=128, null=True)),
                ("last_review_on", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="resources.resource",
                    ),
                ),
                ("isbn", models.CharField(max_length=13, null=True, unique=True)),
                ("authors", models.CharField(max_length=128, null=True)),
                ("publisher", models.CharField(max_length=128, null=True)),
                ("first_published_date", models.DateField(null=True)),
                ("page_count", models.IntegerField(null=True)),
                (
                    "language",
                    models.CharField(default="English", max_length=128, null=True),
                ),
            ],
            bases=("resources.resource",),
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="resources.resource",
                    ),
                ),
                ("course_id", models.CharField(max_length=128, null=True, unique=True)),
                ("course_provider", models.CharField(max_length=128, null=True)),
                ("course_instructor", models.CharField(max_length=128, null=True)),
                ("course_free", models.BooleanField(default=False)),
                (
                    "course_mode_of_instruction",
                    models.CharField(
                        choices=[
                            ("online-recorded", "Online Recorded"),
                            ("online-live", "Online Live"),
                            ("offline", "Offline"),
                            ("text", "Text"),
                            ("mix-text-video", "Mix of Text and Video"),
                            (
                                "mix-text-video-interactivecode",
                                "Mix of Text, Video and Interactive Code",
                            ),
                            (
                                "mix-text-interactivecode",
                                "Mix of Text and Interactive Code",
                            ),
                        ],
                        max_length=128,
                        null=True,
                    ),
                ),
                (
                    "course_duration_scale",
                    models.CharField(
                        choices=[
                            ("hours", "Hours"),
                            ("days", "Days"),
                            ("weeks", "Weeks"),
                            ("months", "Months"),
                            ("years", "Years"),
                        ],
                        max_length=128,
                        null=True,
                    ),
                ),
                ("course_duration_value", models.IntegerField(null=True)),
                ("course_start_date", models.DateField(null=True)),
                ("course_end_date", models.DateField(null=True)),
                (
                    "language",
                    models.CharField(default="English", max_length=128, null=True),
                ),
            ],
            bases=("resources.resource",),
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="resources.resource",
                    ),
                ),
                ("video_id", models.CharField(max_length=128, null=True, unique=True)),
                ("video_provider", models.CharField(max_length=128, null=True)),
                ("channel", models.CharField(max_length=128, null=True)),
                ("upload_date", models.DateField(null=True)),
                ("duration", models.IntegerField(null=True)),
                (
                    "language",
                    models.CharField(default="English", max_length=128, null=True),
                ),
                ("course_sequence", models.IntegerField(null=True)),
                (
                    "course_instance",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resources.course",
                    ),
                ),
            ],
            bases=("resources.resource",),
        ),
    ]
