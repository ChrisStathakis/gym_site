from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class BlogView(ListView):
    template_name = 'blog/index.html'
    model = Blog


class BlogDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
