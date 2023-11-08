from .models import Learner
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

class EmailTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = Learner.EMAIL_FIELD

class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    
class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'is_test_user')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return Learner.objects.create(**validated_data)