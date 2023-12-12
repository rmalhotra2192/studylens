from django.apps import apps
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from studylens_models.models import *

app_models = apps.get_app_config("studylens_models").get_models()

for model in app_models:
    if model.__name__ not in ["Book", "Video", "Course"]:
        admin.site.register(model)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active")
    list_editable = ("active",)
    list_filter = ("language", "active", "last_review_status", "created_at")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active", "course_link")
    list_editable = ("active",)
    list_filter = ("language", "active", "last_review_status", "created_at")

    def course_link(self, obj):
        if obj.course_instance:
            link = reverse(
                "admin:resources_course_change", args=[obj.course_instance.id]
            )
            return format_html('<a href="{}">{}</a>', link, obj.course_instance.title)
        return "-"

    course_link.short_description = "Course"


class VideoInline(admin.StackedInline):
    model = Video
    fk_name = "course_instance"
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active")
    list_editable = ("active",)
    list_filter = ("language", "active", "last_review_status", "created_at")
    inlines = [VideoInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Course, CourseAdmin)
