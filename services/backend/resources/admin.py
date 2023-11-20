from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "cover", "description", "active")
    list_editable = ("active",)
    list_filter = ("language", "active", "last_review_status", "created_at")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "cover", "description", "active", "course_link")
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
    list_display = ("title", "cover", "description", "active")
    list_editable = ("active",)
    list_filter = ("language", "active", "last_review_status", "created_at")
    inlines = [VideoInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Course, CourseAdmin)
