from django.contrib import admin
from .models import *
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('Nome_completo','email','CPF')



