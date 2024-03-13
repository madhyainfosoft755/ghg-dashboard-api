from django.contrib import admin

# Register your models here.
from .models import Population, MWH, GHGEmissionInOman, EmissionIntCO2e

@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'population']

@admin.register(MWH)
class MWHAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'diesel_generators', 'gas', 'solar', 'onshore_wind', 'gas_with_ccs', 'nuclear']

@admin.register(GHGEmissionInOman)
class GHGEmissionInOmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'total_ghg_emission', 'power_consumption', 'renewable_energy_penetration', 'co2_emission']

@admin.register(EmissionIntCO2e)
class EmissionIntCO2eAdmin(admin.ModelAdmin):
    list_display = ['id', 'tco2', 'diesel_generator', 'gas']