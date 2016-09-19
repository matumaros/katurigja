

# from collections import namedtuple
from recordclass import recordclass


Character = recordclass(
    'Character',
    ['id', 'name', 'age', 'band', 'ai', 'speed',
    'characters', 'tiles',]
)
