import math
from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email", "job_type"]
class IdeologistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Ideologist
        fields = "__all__"
class BuilderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Builder
        fields = "__all__"
class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"
class TechnologyBuilderSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(read_only=True)
    builder = BuilderSerializer(read_only=True)
    class Meta:
        model = TechnologyBuilder
        fields = "__all__"
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"
class InterestProjectBuilderSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    builder = BuilderSerializer(read_only=True)
    
    class Meta:
        model = InterestProjectBuilder
        fields = "__all__"