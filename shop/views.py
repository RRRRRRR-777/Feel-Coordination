from multiprocessing import context
from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'index.html', context)