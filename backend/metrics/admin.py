from django.contrib import admin

# Register your models here.
from .models import Server, Metric

admin.site.register(Server)
admin.site.register(Metric)