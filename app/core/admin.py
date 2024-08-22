from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        ('this is the title', {'fields': ('email', 'password')}),
        (
            _('Permission'),
            {
                'fields': (
                    'is_active',
                    'is_superuser',
                    'is_staff',
                )
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'name',
                'password1',
                'password2',
                'is_active',
                'is_superuser',
                'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
