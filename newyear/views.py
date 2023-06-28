import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    next_year = datetime.datetime(now.year +1 , 1, 1)
    gap = next_year - now
    days = gap.days
    return render(request, "newyear/index.html", {
        "newyear" : now.month == 1 and now.day == 1,
        "now" : now,
        "days" : days
    })