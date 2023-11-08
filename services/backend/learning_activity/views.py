from .models import *
from .serializers import *
from root.generic_views import OwnerListView, OwnerDetailView

class ProgDSAListView(OwnerListView):
    queryset = ProgDSA.objects.all().order_by('-created_at')
    serializer_class = ProgDSASerializer
    search_fields = ['title']

class ProgDSADetailView(OwnerDetailView):
    queryset = ProgDSA.objects.all()
    serializer_class = ProgDSASerializer

class ProgSQLListView(OwnerListView):
    queryset = ProgSQL.objects.all().order_by('-created_at')
    serializer_class = ProgSQLSerializer
    search_fields = ['title']

class ProgSQLDetailView(OwnerDetailView):
    queryset = ProgSQL.objects.all()
    serializer_class = ProgSQLSerializer

class ResearchPaperListView(OwnerListView):
    queryset = ResearchPaper.objects.all().order_by('-created_at')
    serializer_class = ResearchPaperSerializer
    search_fields = ['title']

class ResearchPaperDetailView(OwnerDetailView):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

class MockInterviewListView(OwnerListView):
    queryset = MockInterview.objects.all().order_by('-created_at')
    serializer_class = MockInterviewSerializer
    search_fields = ['title']

class MockInterviewDetailView(OwnerDetailView):
    queryset = MockInterview.objects.all()
    serializer_class = MockInterviewSerializer