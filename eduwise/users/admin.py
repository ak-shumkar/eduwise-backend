from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from allauth.socialaccount.models import SocialToken
from allauth.account.models import EmailAddress

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_joined')
    readonly_fields = ('password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email',
                       'is_staff', 'is_active', 'date_joined', 'role', 'groups', 'user_permissions')

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(EmailAddress)
