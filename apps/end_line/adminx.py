# -*- coding: utf-8 -*-

import xadmin
from .models import EndLine


class EndLineAdmin(object):
    search_fields = ['UNIT', 'LINE_ID', 'SENSOR', 'BATTERY', 'RADIO_STATION']
    list_filter = ['SENSOR', 'BATTERY', 'RADIO_STATION', 'TIME', 'TEMPERATURE']


xadmin.site.register(EndLine, EndLineAdmin)
