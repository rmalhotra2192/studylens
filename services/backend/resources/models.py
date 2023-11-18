from django.db import models


# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=128)
    cover = models.CharField(max_length=512, null=True)
    description = models.TextField(null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.IntegerField(null=True)
    internal_rating = models.IntegerField(null=True)


class Book(Resource):
    isbn = models.CharField(max_length=13, unique=True, null=True)
    authors = models.CharField(max_length=128, null=True)
    publisher = models.CharField(max_length=128, null=True)
    first_published_date = models.DateField(null=True)
    page_count = models.IntegerField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")


class Video(Resource):
    video_id = models.CharField(max_length=128, unique=True, null=True)
    video_provider = models.CharField(max_length=128, null=True)
    channel = models.CharField(max_length=128, null=True)
    upload_date = models.DateField(null=True)
    duration = models.IntegerField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")


class Course(Resource):
    course_id = models.CharField(max_length=128, unique=True, null=True)
    course_provider = models.CharField(max_length=128, null=True)
    course_instructor = models.CharField(max_length=128, null=True)
    course_free = models.BooleanField(default=False)
    course_mode_of_instruction = models.CharField(
        choices=[
            ("online-recorded", "Online Recorded"),
            ("online-live", "Online Live"),
            ("offline", "Offline"),
        ],
        max_length=128,
        null=True,
    )
    course_duration_scale = models.CharField(
        choices=[
            ("hours", "Hours"),
            ("days", "Days"),
            ("weeks", "Weeks"),
            ("months", "Months"),
            ("years", "Years"),
        ],
        max_length=128,
        null=True,
    )
    course_duration_value = models.IntegerField(null=True)
    course_start_date = models.DateField(null=True)
    course_end_date = models.DateField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")


class YCourseVideo(Video):
    yt_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_sequence = models.IntegerField(null=True)
