from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('population', views.Population, basename='population')
router.register('mwh', views.MWH, basename='mwh')
router.register('GHGEmissionInOman', views.GHGEmissionInOman, basename='GHGEmissionInOman')
router.register('EmissionIntCO2e', views.EmissionIntCO2e, basename='EmissionIntCO2e')

urlpatterns = [
    path('', include(router.urls)),
]