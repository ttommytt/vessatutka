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
        if (not request.META.get('HTTP_X_DETECTOR') or request.META.get('HTTP_X_DETECTOR') != settings.AUTH_KEY) and request.META.get('REQUEST_METHOD') != 'GET':
            return False
        return True

class MotionDetectionViewSet(viewsets.ModelViewSet):
    queryset = MotionDetection.objects.all().order_by('-timestamp')[:10];
    serializer_class = MotionDetectionSerializer
    permission_classes = [MotionDetectorPermission]
