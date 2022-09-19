from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    watchlist_item = MyWatchList.objects.all()
    context = {
        'list_item': watchlist_item,
        'name': 'Nicole',
        'id': '2106721004',
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")