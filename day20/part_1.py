import numpy as np
from collections import Counter, defaultdict

def img_print(img):
    for row in img:
        for cell in row:
            print(cell, end='')
        print()

# Make a dict of tile_id: tile contents as np array
tiles_lst = open('day20/0.in').read().split('\n\n')
tiles = {}
for tile in tiles_lst:
    tile = tile.splitlines()
    tile_id = int(tile[0].split()[1].removesuffix(':'))
    tiles[tile_id] = np.array([[c for c in row] for row in tile[1:]])

# Grab all the tile edges, make a dict of edge: tile_id
tile_edges = defaultdict(list)
for tile_id, tile in tiles.items():
    for t in [tile, np.transpose(tile)]:
        for _ in range(4):
            tile_edges[''.join(t[0])].append(tile_id)
            t = np.rot90(t)

# Edge tiles have an edge that is unique to them
edge_tiles = [v[0] for v in tile_edges.values() if len(v) == 1]

# Corner tiles are tiles that have two unconnected edges.
# Shows up as count of 4 because each unconnected edge has fwd and reversed versions.
corners = [k for k, v in Counter(edge_tiles).items() if v == 4]
print(np.prod(corners, dtype=np.int64))

assert np.prod(corners, dtype=np.int64) == 30425930368573
print('Tests passed')
