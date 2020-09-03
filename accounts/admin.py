# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and edit users
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    #Controls what is displayed in admin, and what can be filtered
    list_display = ('email', 'first_name', 'last_name', 'npo', 'admin')
    list_filter = ('admin','npo')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('npo', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    #Defines custom fields for admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'npo')}
        ),
    )
    search_fields = ('npo',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


