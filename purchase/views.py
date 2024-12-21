from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from code_warehouse.conf import get_settings
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from app.models import Curso, Profile
from .models import Purchase
import stripe 


settings = get_settings()
stripe.api_key = settings.STRIPE_SECRET_KEY


def init_purchase(request, product_id):
    if not request.user.is_authenticated:
        return redirect('accounts/account_login') 

    product = get_object_or_404(Curso, id=product_id)
    if not product.stripe_price_id:
        return HttpResponseBadRequest("Producto no tiene un precio de Stripe asociado.")

    profile = Profile.objects.get(user=request.user.id) 

    purchase = Purchase.objects.create(
        profile=profile,
        product=product,
    )

    request.session['purchase_id'] = purchase.id  

    success_url = request.build_absolute_uri(reverse('purchase:success'))
    cancel_url = request.build_absolute_uri(reverse('purchase:cancel'))  

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': product.stripe_price_id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )

    purchase.stripe_checkout_session_id = checkout_session.id
    purchase.save()

    return redirect(checkout_session.url)


def success_view(request):
    purchase_id = request.session.get('purchase_id')
    if not purchase_id:
        return HttpResponseBadRequest("No se encontro una compra en la sesion.")

    purchase = get_object_or_404(Purchase, id=purchase_id)
    purchase.completed = True
    purchase.save()

    profile = Profile.objects.get(user=request.user.id)
    curso_id = purchase.product.id
    if profile and purchase_id :
        profile.cursos.add(curso_id)

    return redirect('app:curso', id=curso_id)


def cancel_view(request):
    return HttpResponse(f'Canceled')