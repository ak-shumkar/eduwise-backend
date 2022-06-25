from django.contrib import admin
from .models import Program, Fee, Degree, Faculty, FacultyI18N


class FeeInlineAdmin(admin.TabularInline):
    model = Fee
    exclude = ['institution']


class ProgramAdmin(admin.ModelAdmin):
    inlines = [FeeInlineAdmin]
    fieldsets = (
        (None, {
            'fields': ('title', 'institution', 'degree', 'faculty')
        }),
        ('Extra', {
            'fields': ('website', 'duration')
        }),
        ('Dates', {
            'fields': (('start', 'end'), 'deadline'),
        }),
    )
    list_display = ('title', 'institution', 'degree', 'faculty')

    class Meta:
        model = Program


class FacultyI18NInlineAdmin(admin.TabularInline):
    model = FacultyI18N
    extra = 0


class FacultyAdmin(admin.ModelAdmin):
    inlines = [FacultyI18NInlineAdmin]

    class Meta:
        model = Faculty


admin.site.register(Degree)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Program, ProgramAdmin)
