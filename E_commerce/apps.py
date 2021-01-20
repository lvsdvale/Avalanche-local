from django.apps import AppConfig
from django.conf.urls import url, include
from oscar import config

class MyShop(config.Shop):
    name = 'E_commerce'
    def get_urls(self):
        urlpatterns = [
            url(r'^Catalogo/', self.catalogue_app.urls),
            url(r'^Carrinho/', self.basket_app.urls),
            url(r'^Checkout/', self.checkout_app.urls),
            url(r'^Ofertas/', self.offer_app.urls),
            url(r'^Profile/', self.customer_app.urls),
            url(r'^dashboard/', self.dashboard_app.urls),
            url(r'^Procura/', self.search_app.urls),
            # all the remaining URLs, removed for simplicity
            # ...
        ]
        return urlpatterns


