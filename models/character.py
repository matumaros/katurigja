

# from collections import namedtuple
from recordclass import recordclass


Character = recordclass(
    'Character',
    ['id', 'name', 'age', 'x', 'y', 'ai', 'speed', 'last_pos',
    'characters', 'tiles', 'path',]
)
