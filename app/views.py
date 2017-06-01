from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        render(self.request, self.template_name)
