from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TouristProfile, SOSAlert


# ---------------- USER SERIALIZER ----------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# ---------------- REGISTRATION SERIALIZER ----------------
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# ---------------- TOURIST PROFILE SERIALIZER ----------------
class TouristProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TouristProfile
        fields = '__all__'


# ---------------- SOS ALERT SERIALIZER ----------------
class SOSAlertSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SOSAlert
        fields = ['id', 'user', 'latitude', 'longitude', 'message', 'timestamp']
        read_only_fields = ['user', 'timestamp']
