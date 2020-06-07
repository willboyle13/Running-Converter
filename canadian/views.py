from django.shortcuts import render

# Create your views here.

def canadian(request):
    return render(request, 'canadian/cancalc.html')

def mens(request):
    pass