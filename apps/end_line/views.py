from django.shortcuts import render
from django.views import View
from .models import EndLine
import time


# Create your views here.
class LineTotalView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated():
            unit = user.unit
            auxiliary = EndLine.objects.all().filter(UNIT=unit).order_by("-TIME")
            line = auxiliary[0]
            t = line.TIME
            lines = EndLine.objects.all().filter(TIME=t).order_by("LINE_ID")
            return render(request, "index.html", {"total_lines": lines})
        else:
            return render(request, "login.html")


class LineDetailView(View):
    def get(self, request):
        user = request.user
        unit = user.unit
        line_id = request.GET.get('line_id', '')
        print line_id
        lines = EndLine.objects.all().filter(UNIT=unit, LINE_ID=line_id)

        return render(request, "end_line.html", {"detail_lines": lines})
