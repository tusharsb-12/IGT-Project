from django.urls import path
from .views import map_page, centroids2011

urlpatterns = [
    path('', map_page, name='map-page'),
    path('2011', centroids2011, name='centroids-2011')
]
