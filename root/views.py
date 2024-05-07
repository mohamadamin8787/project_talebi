from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def detales(request):

    return render(request, 'portfolio-details.html')