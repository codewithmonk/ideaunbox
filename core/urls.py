from django.urls import path
from core.views import AwardView, ApparelsView
from core.views import get_home_page, get_apparels

urlpatterns = [
    path('', get_home_page, name="home"),
    path('apparels/', get_apparels, name="apparels"),
    path('awards/', AwardView.as_view(), name="home"),
]