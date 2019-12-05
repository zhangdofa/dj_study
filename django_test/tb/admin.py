from django.contrib import admin

# Register your models here.
from .models import PhoneInfo, Sales

admin.site.register(PhoneInfo)
admin.site.register(Sales)