from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, LearnerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class LearnerView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LearnerSerializer(data=request.data)
        if serializer.is_valid():
            learner = serializer.save()
            if learner:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer