from E_commerce.payment.forms import PaymentMethodForm
from django.views.generic import FormView
from oscar.apps.checkout import exceptions
from oscar.core.loading import get_model, get_class
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from Avalanche import settings

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


        