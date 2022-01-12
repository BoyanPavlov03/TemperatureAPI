from django.shortcuts import render
from elsys.temperatures.api_temperatures import ApiTemperature
# Create your views here.

from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def min_temp(request):
    return JsonResponse(ApiTemperature.min_temp(), safe=False)

def max_temp(request):
    return JsonResponse(ApiTemperature.max_temp(), safe=False)

def avg_temp(request):
    return JsonResponse(ApiTemperature.avg_temp(), safe=False)
