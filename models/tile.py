

from collections import namedtuple


Tile = namedtuple(
    'Tile',
    ['x', 'y', 'altitude', 'ground_type', 'settlement_size', 'resource']
)
