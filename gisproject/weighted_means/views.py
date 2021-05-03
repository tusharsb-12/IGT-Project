import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import IndianStates, Centroids01, Centroids11


def map_page(request):
    return render(request, 'weighted_means/map.html')


def centroids2001(request):
    marker = json.loads(serialize('geojson', Centroids01.objects.all()))
    return HttpResponse(marker)


def centroids2011(request):
    marker = json.loads(serialize('geojson', Centroids11.objects.all()))
    return HttpResponse(marker)
