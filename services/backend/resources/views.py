from studylens_search.search import *
from rest_framework.views import APIView
from rest_framework.response import Response
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, Range

from django.conf import settings


class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        collection_name = "resources_initial_collection_books_500"

        LIMIT_PER_PAGE = 20

        filter_condition = Filter(
            must=[
                FieldCondition(
                    key="type",
                    match={"value": request.query_params["type"]},
                ),
                FieldCondition(
                    key="relevance",
                    match={"value": True},
                ),
                FieldCondition(
                    key="language",
                    match={"value": "English"},
                ),
            ]
        )

        return Response(
            Qdrant_DB(url=settings.QDRANT_HOST, api_key=settings.QDRANT_API_KEY).search(
                collection=collection_name,
                query=request.query_params["query"],
                open_ai_api=OPEN_AI_API(settings.OPENAI_API_KEY),
                limit=LIMIT_PER_PAGE,
                offset=(int(request.query_params["page"]) - 1) * LIMIT_PER_PAGE,
                query_filter=filter_condition,
            )
        )
