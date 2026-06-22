from django.contrib import admin
from .models import Complaint

admin.site.site_header = "Public Service Management Admin"
admin.site.site_title = "PSMS Admin Portal"
admin.site.index_title = "Welcome to PSMS Administration"

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'complaint_id',
        'name',
        'department',
        'status',
        'created_at'
    )

    list_filter = ('status', 'department')
