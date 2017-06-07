from django.shortcuts import render
from django.views.generic import View
from .models import ImageInfo


# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        context = {}
        context['images'] = ImageInfo.objects.all().order_by('-id')
        return render(self.request, self.template_name, context=context)
