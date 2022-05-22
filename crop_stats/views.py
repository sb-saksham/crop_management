from django.views.generic import ListView, View
from django.shortcuts import render


from .models import CropStats


class CropStatsView(ListView):
    model = CropStats
    paginate_by = 20
    template_name = 'crop_stats/crop_stats_home.html'
    context_object_name = 'stat_objs'


def graph_view(request):
    crop_stats = CropStats.objects.all().order_by('crop_health')
    temperature = []
    humidity = []
    sunlight = []
    crop_health = []
    for crop_stat in crop_stats:
        temperature.append(crop_stat.temperature)
        humidity.append(crop_stat.humidity)
        sunlight.append(crop_stat.sunlight)
        crop_health.append(crop_stat.crop_health)
    context = {
        'temperature': temperature,
        'humidity': humidity,
        'sunlight': sunlight,
        'crop_health': crop_health,
    }
    return render(request, 'crop_stats/graph_view.html', context=context)
