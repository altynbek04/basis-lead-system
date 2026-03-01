from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "budget", "score", "is_hot", "status", "created_at")
    list_filter = ("service_type", "is_hot", "status")
    search_fields = ("name", "phone")