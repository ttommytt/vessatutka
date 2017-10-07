# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from vessatutka_api.serializers import *
from vessatutka_api.models import *
from rest_framework import permissions
from django.conf import settings

class MotionDetectorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.META)
        if not request.META.get('HTTP_X_DETECTOR') or request.META.get('HTTP_X_DETECTOR') != settings.AUTH_KEY:
            return False
        return True

class MotionDetectionViewSet(viewsets.ModelViewSet):
    queryset = MotionDetection.objects.all()
    serializer_class = MotionDetectionSerializer
    permission_classes = [MotionDetectorPermission]
