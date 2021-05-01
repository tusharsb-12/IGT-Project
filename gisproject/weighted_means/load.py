import os
from django.contrib.gis.utils import LayerMapping
from .models import IndianStates

indianstates_mapping = {
    'fid': 'FID',
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'nl_name_1': 'NL_NAME_1',
    'varname_1': 'VARNAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'geom': 'MULTIPOLYGON',
}

indian_states_shape = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 'data/indian_states', 'indian_states.shp'),
)


def run(verbose=True):
    lm = LayerMapping(IndianStates, indian_states_shape,
                      indianstates_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)
