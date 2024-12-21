from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('purchase/', include('purchase.urls')),


    path('accounts/', include('allauth.urls')),  #  OAuth operations 
    path('logout/', LogoutView.as_view(), name='logout')  # default Django logout No se usa
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



