from django.shortcuts import render

from rest_framework import viewsets

from .models import Population, MWH, GHGEmissionInOman, EmissionIntCO2e
from .serializers import PopulationSerializer, MWHSerializer, GHGEmissionInOmanSerializer, EmissionIntCO2eSerializer
# Create your views here.

# Create your models here.
class Population(viewsets.ReadOnlyModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

class MWH(viewsets.ReadOnlyModelViewSet):
    queryset = MWH.objects.all()
    serializer_class = MWHSerializer

class GHGEmissionInOman(viewsets.ReadOnlyModelViewSet):
    queryset = GHGEmissionInOman.objects.all()
    serializer_class = GHGEmissionInOmanSerializer

class EmissionIntCO2e(viewsets.ReadOnlyModelViewSet):
    queryset = EmissionIntCO2e.objects.all()
    serializer_class = EmissionIntCO2eSerializer
