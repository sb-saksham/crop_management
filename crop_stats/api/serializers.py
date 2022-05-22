from rest_framework import serializers
from crop_stats.models import CropStats


class CropStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropStats
        fields = [
            'temperature',
            'humidity',
            'sunlight',
            'crop_health',
        ]

    def validate(self, data):
        temperature = data.get("temperature", None)
        humidity = data.get("humidity", None)
        sunlight = data.get("sunlight", None)
        crop_health = data.get("crop_health", None)
        if temperature == "" or humidity == "" or sunlight == "" or crop_health == "":
            raise serializers.ValidationError("All Fields (temperature, humidity, Sunlight and Crop Health) are REQUIRED!!")
        return data
