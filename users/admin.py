from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ( "advisor_name", "advisor_phone_number", "email", "is_staff", "is_active", )
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
            (None, {"fields": ("email", "password", "advisor_name", "advisor_phone_number")}),
            ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})


            )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": (
                    "email", "password1", "password2", "is_staff", "is_active", "groups",
                    "user_permissions", "advisor_name", "advisor_phone_number"

                    )}),

            )
    search_fields = ("advisor_name",)
    ordering = ("advisor_name",)


admin.site.register(CustomUser, CustomUserAdmin)
