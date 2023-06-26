from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email','username', 'age', 'is_staff', ]

    # For displaying in admin panel
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('age',)}),)

    # For add new user in admin panel
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('age',)}),)


admin.site.register(CustomUser, CustomUserAdmin)