from E_commerce.payment.forms import PaymentMethodForm
from django.views.generic import FormView
from oscar.apps.checkout import exceptions
from oscar.core.loading import get_model, get_class
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from Avalanche import settings
from picpay import PicPay
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.shortcuts import render,get_object_or_404,redirect

class CheckCountryPreCondition(object):
    """DRY class for check country in session pre_condition"""

    def get_pre_conditions(self, request):
        if 'check_country_in_session' not in self.pre_conditions:
            return self.pre_conditions + ['check_country_in_session']
        return super().get_pre_conditions(request)

    def check_country_in_session(self, request):
        if request.session.get('country', None) is None:
            raise exceptions.FailedPreCondition(
                    url=reverse('checkout:shipping-address'),
                )


Source = get_model("payment", "Source")
SourceType = get_model("payment", "SourceType")
RedirectRequired = get_class("payment.exceptions", "RedirectRequired")
UnableToPlaceOrder = get_class('order.exceptions', 'UnableToPlaceOrder')
OscarPaymentMethodView = get_class("checkout.views", "PaymentMethodView")
OscarPaymentDetailsView = get_class("checkout.views", "PaymentDetailsView")
OscarShippingMethodView = get_class("checkout.views", "ShippingMethodView")

class PaymentMethodView(OscarPaymentMethodView,FormView):
    template_name = "payment_method.html"
    step = 'payment-method'
    form_class = PaymentMethodForm
    success_url = reverse_lazy('checkout:payment-details')
    
    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured',
        'check_payment_data_is_captured',
    ]
    skip_conditions = ['skip_unless_payment_is_required']

    
    def get(self, request, *args, **kwargs):
        if len(settings.OSCAR_PAYMENT_METHODS) == 1:
            self.checkout_session.pay_by(settings.OSCAR_PAYMENT_METHODS[0][0])
            return redirect(self.get_success_url())
        else:
            return FormView.get(self, request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        # Redirect to the correct payments page as per the method (different methods may have different views &/or additional views)
        return reverse_lazy('checkout:preview')

    def get_initial(self):
        return {
            'payment_method': self.checkout_session.payment_method(),
        }

    def form_valid(self, form):
        # Store payment method in the CheckoutSessionMixin.checkout_session (a CheckoutSessionData object)
        self.checkout_session.pay_by(form.cleaned_data['payment_method'])
        print(self.checkout_session.pay_by)
        return super().form_valid(form)

     

class PicpayView(LoginRequiredMixin, RedirectView):
    login_url = 'Login'
    
    
    def get_redirect_url(self, *args, **kwargs):
        pedidos = get_model('order', 'Order')
        pedidos_pk = self.kwargs.get('pk')
        pedido = get_object_or_404(pedidos.objects.filter(pk = pedidos_pk))
        pc = PicPay(
            x_picpay_token=settings.X_PICPAY_TOKEN, x_seller_token=settings.X_SELLER_TOKEN
        )
        payment = pc.payment(
            reference_id=int(pedido.number),
            callback_url=self.request.build_absolute_uri(reverse('Picpay_Notification',args=[pedidos_pk])),
            return_url=self.request.build_absolute_uri(
            reverse( 'customer:order',args = [int(pedido.number)])
            ),
            value=(float(pedido.total_incl_tax)*1.05),
            buyer={
                "firstName": self.request.user.name,
                "lastName": '',
                "document": self.request.user.CPF,
                "email": self.request.user.email,
                "phone": str(self.request.user.Telefone),
            },
        )
        return payment['paymentUrl']
def PicpayNotification(request,pk):
    if request.method == 'POST':
        pedidos = get_model('order', 'Order')
        pc = PicPay(
            x_picpay_token=settings.X_PICPAY_TOKEN, x_seller_token=settings.X_SELLER_TOKEN
        )
        pedido = pedidos.objects.get(pk=pk)
        status = pc.notification(reference_id=int(pedido.number))
        print(status['status'])
        if status['status'] == 'paid' and pedido.status == 'processando':
                pedido.set_status(new_status='pago')
        return HttpResponse(200)
    else:
        return HttpResponse(404)
