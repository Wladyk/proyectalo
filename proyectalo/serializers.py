from rest_framework import serializers
from .models import *
class SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker
        fields = "__all__"