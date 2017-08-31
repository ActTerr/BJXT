from django.shortcuts import render
from django.views import View
from .models import EndLine
import time


# Create your views here.
class LineTotalView(View):
    def get(self, request):
        unit = request.GET.get("UNIT", '')
        el = getTime()
        lines = EndLine.objects.all().filter(unit=unit, time=el)
        return render(request, "index.html", {"total_lines": lines})


def getTime():
    element_time = time.localtime(time.time())
    hour = time.localtime()[3]
    if hour < 8:
        element_time[2] = element_time[2] - 1
        element_time[3] = 18
    elif 8 < hour < 18:
        element_time[3] = 8
    else:
        element_time[3] = 18

    for i in range(4, 9):
        element_time[i] = 0

    return time.strftime('%Y-%m-%d %H:%M:%S', element_time)


class LineDetailView(View):
    def get(self, request):
        unit = request.GET.get("UNIT", '')
        line_id = request.GET.get('LINE_ID', '')
        lines = EndLine.objects.all().filter(unit=unit, line_id=line_id)

        return render(request, "index.html", {"detail_lines": lines})
