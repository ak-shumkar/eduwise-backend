from django.contrib import admin
from .models import City, Province, Country, CountryI18N, ProvinceI18N, CityI18N


class CityI18NInlineAdmin(admin.TabularInline):
    model = CityI18N


class CityAdmin(admin.ModelAdmin):
    inlines = [CityI18NInlineAdmin]

    class Meta:
        model = City


class CityInlineAdmin(admin.TabularInline):
    model = City


class ProvinceI18NInlineAdmin(admin.TabularInline):
    model = ProvinceI18N


class ProvinceAdmin(admin.ModelAdmin):
    inlines = [ProvinceI18NInlineAdmin, CityInlineAdmin]

    class Meta:
        model = Province


class ProvinceInlineAdmin(admin.TabularInline):
    model = Province


class CountryI18NInlineAdmin(admin.TabularInline):
    model = CountryI18N


class CountryAdmin(admin.ModelAdmin):
    inlines = [CountryI18NInlineAdmin, ProvinceInlineAdmin]

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)
