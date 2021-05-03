from django.urls import path
from .views import map_page, centroids2011, centroids2001

urlpatterns = [
    path('', map_page, name='map-page'),
    path('2001', centroids2001, name='centroids-2001'),
    path('2011', centroids2011, name='centroids-2011')
]
