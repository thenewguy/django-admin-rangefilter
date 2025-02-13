# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class RangeModelDT(models.Model):
    created_at = models.DateTimeField()

    class Meta:
        ordering = ("created_at",)


class RangeModelD(models.Model):
    created_at = models.DateField()

    class Meta:
        ordering = ("created_at",)
