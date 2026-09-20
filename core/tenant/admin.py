from django.contrib import admin

# Register your models here.

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domain', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
