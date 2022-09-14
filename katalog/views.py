from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_catalog_item,
        'name': 'Theirry Nicole Panggabean',
        'id': '2106721004',
    }
    return render(request, "katalog.html", context)