from django.contrib import admin
from django.urls import path

from user.views import current_datetime
from item.views.item import handleItems, handleASpecifcItem
from item.views.category import handleCategories, handleSpecificCategory
from item.views.stock import getStocksFroItem, handleSpecifcStock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', current_datetime),
    path('api/items', handleItems),
    path('api/items/<int:id>', handleASpecifcItem),
    path('api/itemstock/<int:item_id>', getStocksFroItem),
    path('api/stocks/<int:id>', handleSpecifcStock),
    path('api/categories', handleCategories),
    path('api/categories/<int:id>', handleSpecificCategory)
]
