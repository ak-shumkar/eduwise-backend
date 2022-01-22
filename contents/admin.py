from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import Menu, SubMenu, TextBlock, MenuI18N, SubMenuI18N, TextBlockMenuI18N, News, NewsI18N


class TextBlockI18NInlineAdmin(admin.TabularInline):
    model = TextBlockMenuI18N


class TextBlockAdmin(admin.ModelAdmin):
    inlines = [TextBlockI18NInlineAdmin]

    class Meta:
        model = TextBlock


class SubMenuI18NInlineAdmin(admin.TabularInline):
    model = SubMenuI18N


class SubMenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [SubMenuI18NInlineAdmin]
    list_display = ['title', 'order']

    class Meta:
        model = SubMenu


class SubMenuInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = SubMenu


class MenuI18NInlineAdmin(admin.TabularInline):
    model = MenuI18N


class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [MenuI18NInlineAdmin, SubMenuInlineAdmin]
    list_display = ['title', 'order']

    class Meta:
        model = Menu


class NewsI18NInlineAdmin(admin.TabularInline):
    model = NewsI18N
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsI18NInlineAdmin]

    class Meta:
        model = News


admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(News, NewsAdmin)
