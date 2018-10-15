from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = []

