from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]