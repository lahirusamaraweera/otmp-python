from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.category import category
from .models.item import item
from .models.stock import stock

admin.site.register(item)
admin.site.register(category)
admin.site.register(stock)
