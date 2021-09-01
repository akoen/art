import sys

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize = (12,12), constrained_layout = True, dpi = 300)

layers = plot(
    # City name
    '49.2827,-123.1269',

    radius = 2400,

    # Matplotlib 'ax'
    ax = ax,
    layers = {
        'perimeter': {},
        'streets': {
            'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4.5,
                'secondary': 4,
                'tertiary': 3.5,
                'residential': 3,
                'service': 2,
                'unclassified': 2,
                'pedestrian': 2,
                'footway': 1,
            }
        },
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
        'water': {'tags': {'natural': ['water', 'bay']}},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        'forest': {'tags': {'landuse': 'forest'}},
        'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
    },
    drawing_kwargs = {
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
        'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
    },

    osm_credit = {}
)


plt.savefig('./map.png')
plt.savefig('./map.svg')
