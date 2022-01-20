from rest_framework import routers
from proyectalo import viewsets
router = routers.DefaultRouter()
router.register(r'ideologist', viewsets.IdeologistViewset, basename="ideologist")
router.register(r'builder', viewsets.BuilderViewset, basename="builder")

