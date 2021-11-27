import numpy as np

PATTERN = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]

def parse_lines(lines):
    return np.array([[int(bool(c == '#')) for c in row] for row in lines])

def parse_tile(s):
    lines = s.strip().split('\n')
    tile_id = int(lines[0][5:-1])
    tile = parse_lines(lines[1:])
    return tile_id, tile

def tile_mask(tile):
    t = str(tile[0, :])
    rt = str(tile[:, -1])
    b = str(tile[-1, :])
    lt = str(tile[:, 0])
    return (t, rt, b, lt)

def rotations(tile):
    result = []
    for t in [tile, np.transpose(tile)]:
        for i in range(4):
            result.append(t)
            t = np.rot90(t)
    return result

def valid_placements(tile_masks, placed_masks, used_tiles, x, y):
    result = []  # [(tile_id, tile_mask)]
    t = placed_masks.get((x, y - 1))
    rt = placed_masks.get((x + 1, y))
    b = placed_masks.get((x, y + 1))
    lt = placed_masks.get((x - 1, y))
    need = (t and t[2], rt and rt[3], b and b[0], lt and lt[1])
    for tile_id, masks in tile_masks.items():
        if tile_id in used_tiles:
            continue
        for mask in masks:
            if all(need[i] is None or need[i] == mask[i] for i in range(4)):
                result.append((tile_id, mask))
    return result

def stitch(tiles, placed_tiles, placed_masks):
    x0, y0, x1, y1 = bounds(placed_tiles)
    w, h = x1 - x0 + 1, y1 - y0 + 1
    th, tw = tiles[placed_tiles[(x0, y0)]].shape
    th, tw = th - 2, tw - 2
    a = np.zeros((h * th, w * tw))
    for j in range(h):
        for i in range(w):
            x, y = x0 + i, y0 + j
            tile_id = placed_tiles[(x, y)]
            mask = placed_masks[(x, y)]
            for tile in rotations(tiles[tile_id]):
                if tile_mask(tile) == mask:
                    break
            a[j * th: j * th + th, i * tw: i * tw + tw] = tile[1:-1, 1:-1]
    return a

def bounds(positions):
    x0 = min(x for x, y in positions)
    y0 = min(y for x, y in positions)
    x1 = max(x for x, y in positions)
    y1 = max(y for x, y in positions)
    return x0, y0, x1, y1

def count_pattern(im, pattern):
    count = 0
    h, w = im.shape
    ph, pw = pattern.shape
    for y in range(h - ph + 1):
        for x in range(w - pw + 1):
            sub = im[y:y + ph, x:x + pw]
            if np.all(sub[pattern > 0] == 1):
                count += 1
    return count

def run(tiles):
    tile_masks = {}
    for tile_id, tile in tiles.items():
        tile_masks[tile_id] = [tile_mask(a) for a in rotations(tile)]

    placed_tiles = {}  # (x, y) => tile_id
    placed_masks = {}  # (x, y) => (t, r, b, l)
    used_tiles = set()  # {tile_id}

    placed_tiles[(0, 0)] = tile_id
    placed_masks[(0, 0)] = tile_masks[tile_id][0]
    used_tiles.add(tile_id)

    queue = [(0, 0)]
    while queue:
        x, y = queue.pop()
        neighbors = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        for nx, ny in neighbors:
            if (nx, ny) in placed_tiles:
                continue
            valid = valid_placements(
                tile_masks, placed_masks, used_tiles, nx, ny)
            if not valid:
                continue
            tile_id, mask = valid[0]
            placed_tiles[(nx, ny)] = tile_id
            placed_masks[(nx, ny)] = mask
            used_tiles.add(tile_id)
            queue.append((nx, ny))

    # part 1
    x0, y0, x1, y1 = bounds(placed_tiles)
    print(placed_tiles[(x0, y0)] * placed_tiles[(x1, y0)] * placed_tiles[(x0, y1)] * placed_tiles[(x1, y1)])

    # part 2
    im = stitch(tiles, placed_tiles, placed_masks)
    pattern = parse_lines(PATTERN)
    count = max(count_pattern(im, pattern) for im in rotations(im))
    print(np.count_nonzero(im) - count * np.count_nonzero(pattern))

tiles_lst = open('day20/0.in').read().split('\n\n')
tiles = {}
for tile in tiles_lst:
    tile = tile.splitlines()
    tile_id = int(tile[0].split()[1].removesuffix(':'))
    tiles[tile_id] = np.array([[int(bool(c == '#')) for c in row] for row in tile[1:]])

run(tiles)
