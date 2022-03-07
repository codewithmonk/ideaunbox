from django.urls import path
from core.views import AwardView, HomePageView, ApparelsView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('apparels/', ApparelsView.as_view(), name="home"),
    path('awards/', AwardView.as_view(), name="home"),
]