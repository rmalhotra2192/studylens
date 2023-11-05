from .permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import filters
from root.pagination import StandardResultsSetPagination

class OwnerListView(generics.ListCreateAPIView):
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)