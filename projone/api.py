from rest_framework import routers
from proyectalo import viewsets
router = routers.DefaultRouter()
router.register(r'seeker', viewsets.SeekerViewset, basename="seeker")

