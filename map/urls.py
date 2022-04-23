from django.urls import path
from django.urls.resolvers import URLPattern

from .views import municipal_all, city_all, district_all, unit, clear_map

urlpatterns = [
    path('municipal/<str:municipalDistrict>', municipal_all),
    path('city/<str:city>', city_all),
    path('district/<str:cityDistrict>', district_all),
    path('<int:n_mt>', unit),
    path("", clear_map),
]
