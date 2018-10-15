from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email',]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = []

