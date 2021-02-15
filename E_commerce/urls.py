from django.urls import path
from django.conf.urls import include
from .checkout.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path('Checkout/<int:pk>/picpay',PicpayView.as_view(),name = 'Picpay'),
path('Picpay/Notification/<int:pk>',PicpayNotification,name = 'Picpay_Notification')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)