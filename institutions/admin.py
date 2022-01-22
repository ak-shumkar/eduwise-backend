from django.contrib import admin

from programs.admin import FeeInlineAdmin
from .models import Institution, InstitutionType, Deadline


class DeadlineInlineAdmin(admin.TabularInline):
    model = Deadline
    extra = 0


class InstitutionAdmin(admin.ModelAdmin):
    inlines = [FeeInlineAdmin, DeadlineInlineAdmin]
    list_display = ('name', 'city', 'get_province', 'get_country')
    raw_id_fields = ("city",)
    search_fields = ('name', )

    class Meta:
        model = Institution

    @admin.display(ordering='city__province', description='Province')
    def get_province(self, obj):
        return obj.city.province

    @admin.display(ordering='city__country', description='Country')
    def get_country(self, obj):
        return obj.city.country


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(InstitutionType)
