from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .models import item, category
from .model.category import category
from .model.item import item

admin.site.register(item)
admin.site.register(category)
