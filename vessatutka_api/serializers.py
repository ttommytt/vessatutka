from django.contrib.auth.models import User, Group
from rest_framework import serializers
from vessatutka_api.models import *


class MotionDetectionSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True)
    class Meta:
        model = MotionDetection
        fields = ('id', 'timestamp')