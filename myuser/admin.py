from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import People, Assembly
from .forms import UserChangePeopleForm, UserCreationPeopleForm, UserAssemblyChangeForm, UserCreationAssemblyForm


class AccountPeopleAdmin(BaseUserAdmin):
    form = UserChangePeopleForm
    add_form = UserCreationPeopleForm

    list_display = ('contact','first_name', 'last_name', 'town', 'type', 'is_staff', 'is_superuser','is_assembly','is_people')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('contact', 'is_staff', 'is_superuser', 'password','is_assembly','is_people')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'town')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('contact', 'is_staff', 'is_superuser', 'password1', 'password2','is_assembly','is_people')}),
        ('Personal info', {'fields': ('first_name', 'last_name','town')}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('contact', 'first_name','last_name', 'town')
    ordering = ('last_name',)
    filter_horizontal = ()


class AccountAssemblyAdmin(BaseUserAdmin):
    form = UserAssemblyChangeForm
    add_form = UserCreationAssemblyForm

    list_display = ('institution', 'town', 'type', 'is_staff', 'is_superuser','is_assembly','is_people')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('contact', 'is_staff', 'is_superuser', 'password','is_assembly','is_people')}),
        ('Personal info', {'fields': ('institution', 'town')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('contact', 'is_staff', 'is_superuser', 'password1', 'password2','is_assembly','is_people')}),
        ('Personal info', {'fields': ('institution', 'town')}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('contact', 'institution', 'town')
    ordering = ('institution',)
    filter_horizontal = ()


admin.site.register(People, AccountPeopleAdmin)
admin.site.register(Assembly, AccountAssemblyAdmin)
