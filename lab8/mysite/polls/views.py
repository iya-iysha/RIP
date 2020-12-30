from django.shortcuts import render
from django.http import HttpResponse
from . models import Sweet

def index(request):
    sweets = Sweet.objects.all()
    return render(request, 'main/index.html', {'sweets': sweets})

def detail(request, id):
    thesweets = Sweet.objects.filter(id=id)
    return render(request, 'main/detail.html', {'thesweets': thesweets}) 