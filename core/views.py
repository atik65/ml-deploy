
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World from home!")

    return render(request, 'home.html')