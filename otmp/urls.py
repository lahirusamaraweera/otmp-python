from django.contrib import admin
from django.urls import path

from user.views import current_datetime
from item.views.item import handleItems, handleASpecifcItem
from item.views.category import handleCategories, handleSpecificCategory
from item.views.stock import getStocksFroItem, handleSpecifcStock

from authentication.views.authView import handleLogin, handleSignup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', current_datetime),
    path('api/items', handleItems), 
    path('api/items/<int:id>', handleASpecifcItem),
    path('api/itemstock/<int:item_id>', getStocksFroItem),
    path('api/stocks/<int:id>', handleSpecifcStock),
    path('api/categories', handleCategories),
    path('api/categories/<int:id>', handleSpecificCategory),
    path('api/login', handleLogin),
    path('api/register', handleSignup)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
