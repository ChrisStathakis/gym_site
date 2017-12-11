from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *
from gallery.models import *


class ProjectView(ListView):
    template_name = 'projects/index.html'
    model = Project
    paginate_by = 6

    def get_queryset(self):
        queryset = Project.my_query.active_for_site()
        if self.request.GET:
            search_pro = self.request.GET.get('search_name')
            cate_name = self.request.GET.getlist('cate_name')
            queryset = queryset.filter(Q(title__icontains=search_pro) |
                                       Q(category__name__icontains=search_pro)
                                       ).distinct() if search_pro else queryset
            try:
                cates = [Category.objects.get(id=ele) for ele in cate_name]
                queryset = queryset.filter(category__in=cates) if cate_name else queryset
            except:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        search_name = self.request.GET.get('search_name', None)
        cate_name = self.request.GET.getlist('cate_name', None)
        context.update(locals())
        return context


class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        carousel_images = Gallery.objects.all()
        context.update(locals())
        return context