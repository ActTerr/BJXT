# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class EndLine(models.Model):
    UNIT = models.IntegerField(verbose_name=u"单位", null=True, blank=True)
    LINE_ID = models.IntegerField(null=True, blank=True)
    TEMPERATURE = models.IntegerField(verbose_name=u"温度", null=True, blank=True)
    SENSOR = models.IntegerField(verbose_name=u"传感器", choices=((0, u"异常"), (1, u"正常")), null=True, blank=True)
    RADIO_STATION = models.IntegerField(verbose_name=u"电台", choices=((0, u"异常"), (1, u"正常")), null=True, blank=True)
    BATTERY = models.IntegerField(verbose_name=u"电池", choices=((0, u"异常"), (1, u"正常")), null=True, blank=True)
    TIME = models.DateTimeField(verbose_name=u"时间", null=True, blank=True)

    class Meta:
        verbose_name = "尽头线信息"
        verbose_name_plural = verbose_name

