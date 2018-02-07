from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from projects.models import *
from blog.models import *


class Homepage(TemplateView):
    template_name = 'tim/index.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        projects = Project.my_query.first_page()
        blogs = Blog.my_query.active_for_site()[:3]
        trainers = Trainer.objects.filter(active=True, first_page=True)
        context.update(locals())
        return context


