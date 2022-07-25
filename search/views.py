from django.shortcuts import render
from shop.models import Product, Detail
from django.db.models import Q


def search_result(request):
    products = None
    details = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(tags__name__contains=query))
        details = Detail.objects.all().filter(Q(name__contains=query) | Q(tags__name__contains=query))

    return render(request, 'search/search.html', {'query': query, 'products': products, 'details': details})