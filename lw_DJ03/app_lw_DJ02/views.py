from django.shortcuts import render


def index(request):
    return render(request, 'app_lw_DJ02/index.html')


def new(request):
    return render(request, 'app_lw_DJ02/new.html')
