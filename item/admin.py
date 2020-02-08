from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import item, category

admin.site.register(item)
admin.site.register(category)
