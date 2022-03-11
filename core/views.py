from django.shortcuts import render
from django.views.generic import TemplateView
from core.helpers import get_top_apparels, get_catalogue_items, get_filters
# Create your views here.


def get_home_page(request):
    context = {
        "top_apparels": get_top_apparels()
    }
    return render(request, 'home.html', context)

def get_apparels(request, filters=None):
    items = get_catalogue_items("apparels", filters)
    context = {"items": items}
    return render(request, 'catalogue.html', context)


class ApparelsView(TemplateView):
    template_name = 'home.html'

class AwardView(TemplateView):
    template_name = 'home.html'
