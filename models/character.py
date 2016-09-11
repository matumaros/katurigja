

# from collections import namedtuple
from recordclass import recordclass


Character = recordclass(
    'Character',
    ['id', 'name', 'age', 'x', 'y', 'ai', 'characters', 'tiles', 'path']
)
