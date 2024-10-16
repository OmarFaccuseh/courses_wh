from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



