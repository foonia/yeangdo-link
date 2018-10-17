from django.contrib import admin

from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date', 'sex', 'address', 'desired_occupation1']
    list_display_links = ['name']
