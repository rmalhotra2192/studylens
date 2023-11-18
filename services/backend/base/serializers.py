from rest_framework import serializers
from .models import *


class ExternalDataProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalDataProviders
        fields = "__all__"


class ExternalUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalUrls
        fields = "__all__"


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
