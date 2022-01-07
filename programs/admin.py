from django.contrib import admin
from .models import Program, Fee, Degree


class FeeInlineAdmin(admin.TabularInline):
    model = Fee


class ProgramAdmin(admin.ModelAdmin):
    inlines = [FeeInlineAdmin]
    fieldsets = (
        (None, {
           'fields': ('title', 'website', 'duration', 'institution', 'degree')
        }),
        ('Dates', {
            'fields': (('start', 'end'), 'deadline' ),
        }),
    )
    list_display = ('title', 'institution')

    class Meta:
        model = Program


admin.site.register(Degree)
admin.site.register(Program, ProgramAdmin)
