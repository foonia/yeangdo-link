from django.contrib import admin

from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'sex', 'address', 'desired_occupation1', 'final_education', 'desired_salary']
    list_display_links = ['id']
