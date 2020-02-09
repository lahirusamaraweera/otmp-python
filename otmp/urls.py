from django.contrib import admin
from django.urls import path

from user.views import current_datetime
from item.views.item import handleItems, handleSpecifcItem
from item.views.category import handleCategories, handleSpecificCategory
from item.views.stock import getStocksFroItem, handleSpecifcStock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', current_datetime),
    path('items', handleItems),
    path('items/<int:id>', handleSpecifcItem),
    path('itemstock/<int:item_id>', getStocksFroItem),
    path('stocks/<int:id>', handleSpecifcStock),
    path('categories', handleCategories),
    path('categories/<int:id>', handleSpecificCategory)
]
