import stripe
from code_warehouse.conf import get_settings

settings = get_settings()
stripe.api_key = settings.STRIPE_SECRET_KEY

def sale_pipeline(product_name='Test product', price=1000):
    stripe_product_obj = stripe.Product.create(name=product_name)
    stripe_product_id = stripe_product_obj.id 
    stripe_price_obj = stripe.Price.create(
        product = stripe_product_id,
        unit_amount = price,
        currency = 'mxn'
    )
    stripe_price_id = stripe_price_obj.id
    base_endpoint = 'http://127.0.0.1:8000'
    success_url = f'{base_endpoint}/success'
    cancel_url = f'{base_endpoint}/cancel'
    checkout_sesion = stripe.checkout.Session.create(
        line_items = [
            {
                'price' : stripe_price_id,
                'quantity' : 1,
            }
        ],
        mode = 'payment',
        success_url = success_url,
        cancel_url = cancel_url
    )

    print(checkout_sesion.url)
