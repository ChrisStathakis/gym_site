from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *
from gallery.models import *

import datetime


def initial_data():
    trainers = Trainer.objects.filter(active=True, first_page=True)
    return trainers


def filters(request):
    search_pro = request.GET.get('search_name')
    cate_name = request.GET.getlist('cate_name')
    exe_name = request.GET.getlist('exe_name')
    return [search_pro, cate_name, exe_name]


def filter_queryset(queryset, filters_list):
    get_exercises = GymPart.objects.filter(id__in=filters_list[2])
    try:
        queryset = queryset.filter(category__id__in=filters_list[1]) if filters_list[1] else queryset
        queryset = queryset.filter(projectitems__id__in=filters_list[2]).distinct() \
            if filters_list[2] else queryset
        queryset = queryset.filter(Q(title__icontains=filters_list[0]) |
                                   Q(category__name__icontains=filters_list[0])
                                   ).distinct() if filters_list[0] else queryset
    except:
        return queryset
    return queryset


class ProjectView(ListView):
    template_name = '../templates/tim/wodspage.html'
    model = Project
    paginate_by = 20

    def get_queryset(self):
        queryset = Project.my_query.active_for_site()
        search_pro, cate_name, exe_name = filters(self.request)
        queryset = filter_queryset(queryset, [search_pro, cate_name, exe_name])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        categories, exercises = Category.objects.all(), GymPart.objects.all()
        search_pro, cate_name, exe_name = filters(self.request)
        trainers = initial_data()
        featured_exercises = Project.objects.filter(active=True, first_page=True)
        date = datetime.datetime.now()
        context.update(locals())
        return context


class ProjectDetailView(DetailView):
    template_name = '../templates/tim/wod-detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        carousel_images = Gallery.objects.all()
        trainers = initial_data()
        context.update(locals())
        return context