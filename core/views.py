from django.shortcuts import render
from django.views.generic import TemplateView
from core.helpers import get_top_apparels
# Create your views here.


def get_home_page(request):
    context = {
        "top_apparels": get_top_apparels()
    }
    return render(request, 'home.html', context)


class ApparelsView(TemplateView):
    template_name = 'home.html'

class AwardView(TemplateView):
    template_name = 'home.html'
