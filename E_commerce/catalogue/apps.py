import oscar.apps.catalogue.apps as apps
from django.conf.urls import include, url

class CatalogueConfig(apps.CatalogueConfig):
    name = 'E_commerce.catalogue'

