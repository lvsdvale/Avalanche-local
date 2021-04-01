from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
@admin.register(posts)
class admin_posts(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    list_display = ('name', 'pub_date')
    search_fields = ('name','pub_date')


