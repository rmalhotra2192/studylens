from django.urls import path, include
from .views import LearnerView
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenObtainPairView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', LearnerView.as_view(), name='register'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]