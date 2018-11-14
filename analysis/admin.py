from django.contrib import admin

from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'sex', 'address', 'desired_salary']
    list_display_links = ['name']
