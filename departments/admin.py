from django.contrib import admin

# Register your models here.
from .models import department, faculty

admin.site.register(department)
admin.site.register(faculty)
