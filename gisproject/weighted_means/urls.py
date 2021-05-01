from django.urls import path
from .views import map_page, map_boundaries

urlpatterns = [
    path('', map_page, name='map-page'),
    path('boundary', map_boundaries, name='boundaries')
]
