from pydoc import pager
from django.shortcuts import render
from django.views.generic import TemplateView
from core.helpers import get_top_apparels, get_catalogue_items, get_filters, get_product_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def get_home_page(request):
    context = {
        "top_apparels": get_top_apparels()
    }
    return render(request, 'home.html', context)

def paginate_items(items, request):
    paginator = Paginator(items, 20)
    page = request.GET.get('page', 1)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    return records


def get_apparels(request, filters=None):
    # TODO: implement filtering and object querying
    items = get_catalogue_items("apparels", filters)
    records = paginate_items(items, request)
    context = {"items": records}
    # TODO: return filters available for each category vs applied
    return render(request, 'catalogue.html', context)

def get_individual_item(request, slug):
    item = get_product_detail(slug)
    context = {"item": item}
    return render(request, 'product.html', context)


class ApparelsView(TemplateView):
    template_name = 'home.html'

class AwardView(TemplateView):
    template_name = 'home.html'
