from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from docs.swagger import schema_view


urlpatterns = [
    path('admin', admin.site.urls),
    path('currencies', include('currencies.urls'))
]

if settings.DEBUG:
    urlpatterns += [path('swagger', schema_view.with_ui('swagger', cache_timeout=0))]
