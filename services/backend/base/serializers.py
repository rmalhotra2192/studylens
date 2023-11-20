from rest_framework import serializers
from .models import *


class ExternalDataProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalDataProvider
        fields = "__all__"


class ExternalUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalUrl
        fields = "__all__"


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
