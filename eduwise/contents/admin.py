from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from . import models


class TextBlockI18NInlineAdmin(admin.TabularInline):
    model = models.TextBlockMenuI18N


class TextBlockAdmin(admin.ModelAdmin):
    inlines = [TextBlockI18NInlineAdmin]

    class Meta:
        model = models.TextBlock


class SubMenuI18NInlineAdmin(admin.TabularInline):
    model = models.SubMenuI18N


class SubMenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [SubMenuI18NInlineAdmin]
    list_display = ['title', 'order']

    class Meta:
        model = models.SubMenu


class SubMenuInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = models.SubMenu


class MenuI18NInlineAdmin(admin.TabularInline):
    model = models.MenuI18N


class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [MenuI18NInlineAdmin, SubMenuInlineAdmin]
    list_display = ['title', 'order']

    class Meta:
        model = models.Menu


class NewsI18NInlineAdmin(admin.TabularInline):
    model = models.NewsI18N
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsI18NInlineAdmin]

    class Meta:
        model = models.News


class ProcessI18NInlineAdmin(admin.TabularInline):
    model = models.ProcessI18N
    extra = 0


class ProcessAdmin(admin.ModelAdmin):
    inlines = [ProcessI18NInlineAdmin]

    class Meta:
        model = models.Process


admin.site.register(models.TextBlock, TextBlockAdmin)
admin.site.register(models.SubMenu, SubMenuAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Process, ProcessAdmin)
