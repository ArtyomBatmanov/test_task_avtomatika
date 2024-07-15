from django.contrib import admin
from .models import Worker, Store, Visit

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ['worker__name', 'store__name']
