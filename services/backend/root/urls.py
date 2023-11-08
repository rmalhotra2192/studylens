from django.urls import path
from .views import *
from rest_framework import generics

urlpatterns = [
    path('tags/', TagsListView.as_view(), name='tags_list'),
    path('tags/<int:pk>/', TagsDetailView.as_view(), name='tags_detail'),
]