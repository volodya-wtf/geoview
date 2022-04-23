from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.widgets import AutocompleteSelect

from .models import Customer
from .models import Unit

from django import forms


class UnitAdmin(admin.ModelAdmin):
    list_display = ("municipalDistrict", "cityDistrict", "city", "address", "n_mt")
    list_display_links = ("n_mt",)
    search_fields = ("municipalDistrict", "cityDistrict", "city", "address", "n_mt")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","municipalDistrict", "city", "cityDistrict", "prefix", "street", "building", "postfix", "unit")
    list_display_links = ("id","unit",)
    search_fields = ("unit__n_mt", "municipalDistrict", "city", "cityDistrict", "prefix", "street", "building", "postfix")
    autocomplete_fields = [
        "unit",
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Unit, UnitAdmin)
