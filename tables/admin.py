from django.contrib import admin
from .models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "count_of_seats",)
    search_fields = ("name",)
