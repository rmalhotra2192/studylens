from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from root.pagination import StandardResultsSetPagination

class ProgDSAListView(generics.ListAPIView):
    queryset = ProgDSA.objects.all().order_by('-created_at')
    serializer_class = ProgDSASerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ProgDSADetailView(generics.RetrieveUpdateAPIView):
    queryset = ProgDSA.objects.all()
    serializer_class = ProgDSASerializer

class ProgSQLListView(generics.ListAPIView):
    queryset = ProgSQL.objects.all().order_by('-created_at')
    serializer_class = ProgSQLSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ProgSQLDetailView(generics.RetrieveUpdateAPIView):
    queryset = ProgSQL.objects.all()
    serializer_class = ProgSQLSerializer

class ResearchPaperListView(generics.ListAPIView):
    queryset = ResearchPaper.objects.all().order_by('-created_at')
    serializer_class = ResearchPaperSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ResearchPaperDetailView(generics.RetrieveUpdateAPIView):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

class MockInterviewListView(generics.ListAPIView):
    queryset = MockInterview.objects.all().order_by('-created_at')
    serializer_class = MockInterviewSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class MockInterviewDetailView(generics.RetrieveUpdateAPIView):
    queryset = MockInterview.objects.all()
    serializer_class = MockInterviewSerializer