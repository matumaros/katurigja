

from recordclass import recordclass


Band = recordclass(
    'Band',
    ['id', 'name', 'leader', 'pos', 'last_pos', 'speed', 'characters', 'path',]
)
