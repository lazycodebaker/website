from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class Certificate(admin.ModelAdmin):
    list_display = ['enrollment_id', 'username','verified', 'certificate']

