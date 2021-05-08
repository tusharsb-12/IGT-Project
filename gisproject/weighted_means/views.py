import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import IndianStates, Centroids01, Centroids11


def map_page_2001(request):
    return render(request, 'weighted_means/map_2001.html')


def map_page_2011(request):
    return render(request, 'weighted_means/map_2011.html')


def map_page(request):
    return render(request, 'weighted_means/map.html')


def centroids2001(request):
    markers = json.loads(serialize('geojson', Centroids01.objects.all()))
    return JsonResponse(markers)


def centroids2011(request):
    marker = json.loads(serialize('geojson', Centroids11.objects.all()))
    return JsonResponse(marker)
