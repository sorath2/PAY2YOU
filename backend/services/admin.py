from django.contrib import admin

from .models import (CategoryImage, CategoryService, Service,
                     ServiceCategoryImage, Tariff, TariffCondition,
                     TariffSpecialCondition, TariffTrialPeriod)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCategoryImage)
class ServiceCategoryImageAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(TariffSpecialCondition)
class TariffSpecialConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(TariffCondition)
class TariffConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(TariffTrialPeriod)
class TariffTrialPeriodAdmin(admin.ModelAdmin):
    pass
