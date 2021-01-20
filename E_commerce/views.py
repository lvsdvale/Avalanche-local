from picpay import PicPay
from Avalanche import settings
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from oscar.core.loading import  get_model
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
@csrf_exempt
def picpay_payment(request,pk):
    basket_model = get_model('basket', 'Basket')
    Basket = get_object_or_404(basket_model.objects.filter(pk=pk))
    pc = PicPay(
        x_picpay_token=settings.X_PICPAY_TOKEN, x_seller_token=settings.X_SELLER_TOKEN
    )
    payment = pc.payment(
        reference_id=Basket.pk+107,
        callback_url= 'http://localhost:8000/',
        return_url=request.build_absolute_uri(
            reverse('checkout:preview')
            )
        ,
        value=float(request.basket.total_incl_tax)*1.1,
        buyer={
            "firstName":request.user.name,
            "lastName": request.user.name,
            "document": request.user.CPF,
            "email": request.user.email,
            "phone": str(request.user.Telefone),
        },
    )
    return HttpResponseRedirect(payment['paymentUrl'])