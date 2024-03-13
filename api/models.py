from django.db import models

# Create your models here.
class Population(models.Model):
    year = models.IntegerField()
    population = models.BigIntegerField()

class MWH(models.Model):
    year = models.IntegerField()
    diesel_generators = models.FloatField()
    gas = models.FloatField()
    solar = models.FloatField()
    onshore_wind = models.FloatField()
    gas_with_ccs = models.FloatField()
    nuclear =models.FloatField()

class GHGEmissionInOman(models.Model):
    year = models.IntegerField()
    # total_ghg_emission (in mtco2eq)
    total_ghg_emission = models.BigIntegerField()
    # power_consumption in mwh
    power_consumption = models.BigIntegerField()
    # renewable_energy_penetration in percentage
    renewable_energy_penetration = models.IntegerField()
    # co2_emission per population (tco2/capita)
    co2_emission = models.BigIntegerField()

class EmissionIntCO2e(models.Model):
    tco2 = models.IntegerField()
    diesel_generator = models.BigIntegerField()
    gas = models.BigIntegerField()