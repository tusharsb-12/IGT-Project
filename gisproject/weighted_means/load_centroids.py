import os
import pandas as pd
from django.contrib.gis.geos import fromstr
from weighted_means.models import Centroids01, Centroids11


def save_centroids_2001():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     'centroids_data', 'results_2001.csv'))

    for i in df.index:
        # print(f'{df.State[i]} {df.Longitude[i]} {df.Latitude[i]}')
        state = df.State[i]
        longitude = df.Longitude[i]
        latitude = df.Latitude[i]
        location = fromstr(f'POINT({longitude} {latitude})', srid=4326)

        Centroids01(state=state, location=location).save()


def save_centroids_2011():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     'centroids_data', 'results_2011.csv'))

    for i in df.index:
        # print(f'{df.State[i]} {df.Longitude[i]} {df.Latitude[i]}')
        state = df.State[i]
        longitude = df.Longitude[i]
        latitude = df.Latitude[i]
        location = fromstr(f'POINT({longitude} {latitude})', srid=4326)

        Centroids11(state=state, location=location).save()
