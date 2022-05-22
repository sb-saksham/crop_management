from rest_framework.generics import CreateAPIView

from .serializers import CropStatSerializer
from crop_stats.models import CropStats


class CropStatAPIView(CreateAPIView):
    serializer_class = CropStatSerializer

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

