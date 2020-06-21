from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(posts)
class admin_posts(admin.ModelAdmin):
    list_display = ('name', 'pub_date')


