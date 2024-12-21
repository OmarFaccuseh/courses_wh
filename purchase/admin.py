from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    fields = ['profile','product','stripe_checkout_session_id','completed','stripe_price','timestamp', 'previous_stripe_price']
    readonly_fields = ['stripe_checkout_session_id', 'previous_stripe_price', 'timestamp']

admin.site.register(Purchase, PurchaseAdmin)