from django.db import models
from app.models import Profile, Curso

class Purchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)
    stripe_checkout_session_id = models.CharField(max_length=220, null=True, blank=True)
    completed = models.BooleanField(default=False)
    stripe_price = models.IntegerField(default=0)
    previous_stripe_price = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)