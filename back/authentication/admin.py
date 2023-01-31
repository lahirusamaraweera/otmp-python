from django.contrib import admin


from .models.user import user
from .models.authToken import authToken

admin.site.register(user)
admin.site.register(authToken)

