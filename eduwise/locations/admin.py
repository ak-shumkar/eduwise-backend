from django.contrib import admin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models import City, Province, Country, CountryI18N, ProvinceI18N, CityI18N
from .forms import CountryForm, CityForm


class CityI18NInlineAdmin(admin.TabularInline):
    model = CityI18N
    extra = 0


class CityAdmin(admin.ModelAdmin):
    form = CityForm
    inlines = [CityI18NInlineAdmin]
    list_display = ("name", 'province', 'country')
    search_fields = ("name", 'province__name', 'country__name')
    list_filter = (
        ('province', RelatedDropdownFilter),
        ('country', RelatedDropdownFilter),
    )

    class Meta:
        model = City


class CityInlineAdmin(admin.TabularInline):
    model = City
    extra = 0


class ProvinceI18NInlineAdmin(admin.TabularInline):
    model = ProvinceI18N
    extra = 0


class ProvinceAdmin(admin.ModelAdmin):
    inlines = [ProvinceI18NInlineAdmin, CityInlineAdmin]
    list_display = ('name', 'country')
    search_fields = ("name", )
    list_filter = (
        ('country', RelatedDropdownFilter),
    )

    class Meta:
        model = Province


class ProvinceInlineAdmin(admin.TabularInline):
    model = Province
    extra = 0


class CountryI18NInlineAdmin(admin.TabularInline):
    model = CountryI18N
    extra = 0


class CountryAdmin(admin.ModelAdmin):
    inlines = [CountryI18NInlineAdmin, ProvinceInlineAdmin]
    form = CountryForm
    list_display = ['name', 'iso_code']
    search_fields = ("name", )


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)
