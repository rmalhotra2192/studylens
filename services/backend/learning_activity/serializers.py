from rest_framework import serializers
from .models import ProgDSA, ProgSQL, MockInterview, ResearchPaper

class ProgDSASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgDSA
        fields = "__all__"

class ProgSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgSQL
        fields = "__all__"

class MockInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockInterview
        field = "__all__"

class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        field = "__all__"
