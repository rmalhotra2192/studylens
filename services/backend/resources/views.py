# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch_dsl import MultiSearch, Search


class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get("q", "")
        if query:
            multi_search = MultiSearch(
                index=["resources", "books", "videos", "courses"]
            )
            search_query = Search().query("match", title=query)
            multi_search = multi_search.add(search_query)

            responses = multi_search.execute()
            results = [response.to_dict() for response in responses]

            return Response(results)
        return Response({"message": "No query provided"}, status=400)
