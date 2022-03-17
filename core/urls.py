from django.urls import path
from core.views import AwardView, ApparelsView
from core.views import get_home_page, get_apparels, get_individual_item

urlpatterns = [
    path('', get_home_page, name="home"),
    path('apparels/', get_apparels, name="apparels"),
    path('awards/', AwardView.as_view(), name="home"),
    path('apparels/product/<slug>', get_individual_item, name="individual"),
]