from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from .pagination import StandardResultsSetPagination
from root.generic_views import OwnerListView, OwnerDetailView


class TagsListView(OwnerListView):
    queryset = Tags.objects.all().order_by('-created_at')
    serializer_class = TagsSerializer
    search_fields = ['title']

class TagsDetailView(OwnerDetailView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class LearningGoalsListView(OwnerListView):
    queryset = LearningGoals.objects.all().order_by('-created_at')
    serializer_class = LearningGoalsSerializer
    search_fields = ['goal_name']

class LearningGoalsDetailView(OwnerDetailView):
    queryset = LearningGoals.objects.all()
    serializer_class = LearningGoalsSerializer

class LearningTopicsListView(OwnerListView):
    queryset = LearningTopics.objects.all().order_by('-created_at')
    serializer_class = LearningTopicsSerializer
    search_fields = ['topic_name']

class LearningTopicsDetailView(OwnerDetailView):
    queryset = LearningTopics.objects.all()
    serializer_class = LearningTopicsSerializer