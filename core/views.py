from django.shortcuts import render
from django.views.generic import TemplateView
from core.helpers import get_top_apparels, get_catalogue_items, get_filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def get_home_page(request):
    context = {
        "top_apparels": get_top_apparels()
    }
    return render(request, 'home.html', context)

def get_apparels(request, filters=None):
    items = get_catalogue_items("apparels", filters)
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 20)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    # context['items'] = records
    context = {"items": records}
    # TODO: return filters available for each category vs applied
    return render(request, 'catalogue.html', context)


class ApparelsView(TemplateView):
    template_name = 'home.html'

class AwardView(TemplateView):
    template_name = 'home.html'
