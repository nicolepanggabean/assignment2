from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist_item = MyWatchList.objects.all()

    watched = 0
    unwatched = 0

    for item in data_watchlist_item:
        if item.watched == True:
            watched += 1
        else:
            unwatched += 1

    context = {
        'name': 'Nicole',
        'id': '2106721004',
        'list_item': data_watchlist_item,
        'watched': watched,
        'unwatched': unwatched,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")