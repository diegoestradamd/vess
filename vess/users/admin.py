from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import HealthCareUserCreationForm, HealthCareUserChangeForm
from .models import HealthCareUser

class HealthCareUserAdmin(UserAdmin):

    form = HealthCareUserChangeForm
    add_form = HealthCareUserCreationForm
    list_display = ('id', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal Informarion', {'fields': ('id', 'first_name', 'last_name', 'email', 'role')})
    )
    search_fields = ('username', 'id', 'first_name', 'last_name', 'email')
    ordering = ('id',)    

admin.site.register(HealthCareUser, HealthCareUserAdmin)