import rest_framework
from rest_framework import viewsets
from proyectalo.models import *
from . import serializers
import datetime
import json
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
class IdeologistViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.IdeologistSerializer
    queryset = Ideologist.objects.all()
class BuilderViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BuilderSerializer
    queryset = Builder.objects.all()
