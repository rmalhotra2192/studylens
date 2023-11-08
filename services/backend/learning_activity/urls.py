from django.urls import path
from .views import *
from rest_framework import generics

urlpatterns = [
    path('dsa/', ProgDSAListView.as_view(), name='dsa_list'),
    path('dsa/<int:pk>/', ProgDSADetailView.as_view(), name='dsa_detail'),
    path('sql/', ProgSQLListView.as_view(), name='sql_list'),
    path('sql/<int:pk>/', ProgSQLDetailView.as_view(), name='sql_detail'),
    path('research_papers/', ResearchPaperListView.as_view(), name='research_list'),
    path('research_paper/<int:pk>/', ResearchPaperDetailView.as_view(), name='research_detail'),
    path('mockinterviews/', MockInterviewListView.as_view(), name='mocki_list'),
    path('mockinterview/<int:pk>/', MockInterviewDetailView.as_view(), name='mocki_detail'),
]