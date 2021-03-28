from django.contrib import admin
from LenteCup import models
from .forms import WeekForm, ScoresForm


@admin.register(models.Week)
class WeekAdmin(admin.ModelAdmin):
    form = WeekForm
    list_display = ["week"]


@admin.register(models.Scores)
class ScoresAdmin(admin.ModelAdmin):
    form = ScoresForm
    list_display = ['user', 'week', 'score', 'qualifying', 'baan', 'lus']