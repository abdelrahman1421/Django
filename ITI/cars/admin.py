from django.contrib import admin

# Register your models here.
from cars.models import Car, FactorInformation


class CustomCar(admin.ModelAdmin):
    fieldsets = (
        ['Car Information', {'fields': ['name', 'markName', 'model']}],
        ['Factory Information', {'fields': ['factoryInfo']}],

    )
    list_display = ('name', 'markName', 'model','factoryInfo','modelChek','createdAt','updatedAt')


admin.site.register(Car, CustomCar)
admin.site.register(FactorInformation)
