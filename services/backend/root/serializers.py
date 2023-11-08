from rest_framework import serializers
from .models import Tags, LearningGoals, LearningTopics

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"

class LearningGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningGoals
        fields = "__all__"

class LearningTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTopics
        fields = "__all__"