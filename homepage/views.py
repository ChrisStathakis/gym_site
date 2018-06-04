from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from projects.models import *
from blog.models import *


def initial_data():
    trainers = Trainer.objects.filter(active=True, first_page=True)
    return trainers


class Homepage(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        projects = Project.my_query.first_page()
        blogs = Blog.my_query.active_for_site()[:3]
        trainers = initial_data()
        context.update(locals())
        return context


class ServiceView(TemplateView):
    template_name = 'homepage/service_page.html'


class ProgramsView(ListView):
    template_name = 'homepage/programs_page.html'
    model = GymPart


class AboutPage(TemplateView):
    template_name = 'homepage/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        trainers = initial_data()
        context.update(locals())
        return context


class TrainerPage(DetailView):
    model = Trainer
    template_name = 'tim/trainer_page.html'

    def get_context_data(self, **kwargs):
        context = super(TrainerPage, self).get_context_data(**kwargs)
        trainers = initial_data()
        context.update(locals())
        return context