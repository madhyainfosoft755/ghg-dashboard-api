from rest_framework import serializers

from .models import Population, MWH, GHGEmissionInOman, EmissionIntCO2e

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = "__all__"

class MWHSerializer(serializers.ModelSerializer):
    class Meta:
        model = MWH
        fields = "__all__"

class GHGEmissionInOmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GHGEmissionInOman
        fields = "__all__"

class EmissionIntCO2eSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionIntCO2e
        fields = '__all__'