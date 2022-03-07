from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class ApparelsView(TemplateView):
    template_name = 'home.html'

class AwardView(TemplateView):
    template_name = 'home.html'
