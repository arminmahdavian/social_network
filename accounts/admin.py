from django.contrib import admin
from .models import Profile, Country

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
