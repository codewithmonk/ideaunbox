from django.urls import path
from core.views import AwardView, ApparelsView
from core.views import get_home_page

urlpatterns = [
    path('', get_home_page, name="home"),
    path('apparels/', ApparelsView.as_view(), name="home"),
    path('awards/', AwardView.as_view(), name="home"),
]