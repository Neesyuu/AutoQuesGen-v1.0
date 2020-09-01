from django.shortcuts import render


# Create your views here.


def indexView(request):
    return render(request, 'home/index.html')


def csView(request):
    return render(request, 'comingsoon.html')
