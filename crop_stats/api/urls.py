from django.urls import path
from .views import CropStatAPIView

urlpatterns = [
    path('', CropStatAPIView.as_view()),
]
