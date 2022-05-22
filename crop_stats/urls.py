from django.urls import path, include
from .views import CropStatsView, graph_view

app_name = 'crop_stats'

urlpatterns = [
    path('', CropStatsView.as_view(), name='home'),
    path('graph/', graph_view, name='graph'),
]
