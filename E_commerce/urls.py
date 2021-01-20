from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path('Checkout/<int:pk>/picpay',picpay_payment,name = 'Picpay'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)