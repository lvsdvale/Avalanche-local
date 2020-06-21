from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import View,TemplateView,FormView
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
# Create your views here.
def Blog(request):
    Posts_list = posts.objects.all().order_by('-pub_date')
    paginator = Paginator(Posts_list, 10)
    page = request.GET.get('page')
    Posts = paginator.get_page(page)
    context = {"Posts": Posts
               }
    return render(request, 'Blog.html', context)

class Post_view(DetailView):
    model = posts
    template_name = 'PadraoPosts.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'