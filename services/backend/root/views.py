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