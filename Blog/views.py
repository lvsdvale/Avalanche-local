from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import View,TemplateView,FormView,ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
# Create your views here.
class Blog(ListView):
    template_name = 'Blog.html'
    model = posts
    paginate_by = 10
    ordering = '-pub_date'

class Post_view(DetailView):
    model = posts
    template_name = 'PadraoPosts.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'