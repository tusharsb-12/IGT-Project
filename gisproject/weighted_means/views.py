import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.gis.db.models.functions import AsGeoJSON
from .models import IndianStates


def map_page(request):
    return render(request, 'weighted_means/map.html')


def map_boundaries(request):
    states = IndianStates.objects.annotate(
        json=AsGeoJSON('geom')).get(name_1='Maharashtra').json
    return HttpResponse(states, content_type='json')
