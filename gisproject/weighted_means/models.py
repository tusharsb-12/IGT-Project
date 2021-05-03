from django.contrib.gis.db import models


class IndianStates(models.Model):
    fid = models.IntegerField()
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=5)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=22)
    nl_name_1 = models.CharField(max_length=1, null=True)
    varname_1 = models.CharField(max_length=100, null=True)
    type_1 = models.CharField(max_length=14)
    engtype_1 = models.CharField(max_length=15)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Indian States'

    def __str__(self):
        return self.name_1


class Centroids01(models.Model):
    state = models.CharField(max_length=100)
    location = models.PointField()

    class Meta:
        verbose_name_plural = 'Centroids 2001'

    def __str__(self):
        return self.state


class Centroids11(models.Model):
    state = models.CharField(max_length=100)
    location = models.PointField()

    class Meta:
        verbose_name_plural = 'Centroids 2011'

    def __str__(self):
        return self.state
