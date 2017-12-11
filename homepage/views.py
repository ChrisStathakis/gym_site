from django.shortcuts import render
from django.views.generic import View

from projects.models import *
from blog.models import *


class Homepage(View):
    template_name = 'index.html'

    def get(self, request):
        projects = Project.my_query.first_page()
        blogs = Blog.my_query.active_for_site()[:3]
        context = locals()
        return render(request, self.template_name, context)


class CostCalculator(View):
    template_name = 'cost.html'
