from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "status"]


admin.site.register(CustomUser, CustomUserAdmin)
