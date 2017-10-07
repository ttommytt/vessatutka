# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MotionDetection(models.Model):
	timestamp = models.DateTimeField(auto_now=True)

# Create your models here.
