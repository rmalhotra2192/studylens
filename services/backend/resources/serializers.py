from rest_framework import serializers
from .models import *


class ExternalDataProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ExternalUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class ExternalMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ExternalMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YCourseVideo
        fields = "__all__"
