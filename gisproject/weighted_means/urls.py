from django.urls import path
from .views import map_page_2001, map_page_2011, centroids2011, centroids2001, map_page

urlpatterns = [
    path('map/', map_page, name='map-page'),
    path('map/2001', map_page_2001, name='map-page_2001'),
    path('map/2011', map_page_2011, name='map-page_2011'),
    path('2001', centroids2001, name='centroids-2001'),
    path('2011', centroids2011, name='centroids-2011')
]
