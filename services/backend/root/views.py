from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from .pagination import StandardResultsSetPagination

class TagsListView(generics.ListAPIView):
    queryset = Tags.objects.all().order_by('-created_at')
    serializer_class = TagsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['tag_display']

class TagsDetailView(generics.RetrieveUpdateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class LearningGoalsListView(generics.ListAPIView):
    queryset = LearningGoals.objects.all().order_by('-created_at')
    serializer_class = LearningGoalsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['goal_name']

class LearningGoalsDetailView(generics.RetrieveUpdateAPIView):
    queryset = LearningGoals.objects.all()
    serializer_class = LearningGoalsSerializer

class LearningTopicsListView(generics.ListAPIView):
    queryset = LearningTopics.objects.all().order_by('-created_at')
    serializer_class = LearningTopicsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic_name']

class LearningTopicsDetailView(generics.RetrieveUpdateAPIView):
    queryset = LearningTopics.objects.all()
    serializer_class = LearningTopicsSerializer