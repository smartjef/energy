from django.contrib import admin
from .models import Company, EnergyConsumption
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'website', 'email']
    list_filter = ['created','updated']
    search_fields = ['name','address', 'phone_number','website', 'email']

@admin.register(EnergyConsumption)
class EnergyConsumptionAdmin(admin.ModelAdmin):
    list_display = ['company', 'amount', 'date', 'created', 'updated']
    list_filter = ['created','updated']
    search_fields = ['company','amount']
