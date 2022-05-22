from django.db import models


class CropStats(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    sunlight = models.IntegerField()
    crop_health = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Recorded at {self.time}'
