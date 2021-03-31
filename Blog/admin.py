from django.contrib import admin
from .models import *

@admin.register(posts)
class admin_posts(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name','pub_date')


