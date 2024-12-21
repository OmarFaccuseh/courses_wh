from django.urls import path
from . import views

app_name = 'purchase' 

urlpatterns = [
    path('init_purchase/<int:product_id>', views.init_purchase, name='init_purchase'),
    path('success', views.success_view, name='success'),
    path('cancel', views.cancel_view, name='cancel'),
]
