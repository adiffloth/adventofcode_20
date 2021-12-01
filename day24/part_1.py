from collections import defaultdict

lines = [list(x) for x in open('day24/0.in').read().splitlines()]

def neighbors(tile):
    y, x = tile
    return set([(y - 1, x + 1), (y - 1, x), (y, x - 1), (y + 1, x - 1), (y + 1, x), (y, x + 1)])

black_tiles = set()
for line in lines:
    y = x = 0
    while line:
        c = line.pop(0)
        if c == 'n':
            c2 = line.pop(0)
            if c2 == 'e':
                y -= 1
                x += 1
            else:
                y -= 1
        elif c == 'w':
            x -= 1
        elif c == 's':
            c2 = line.pop(0)
            if c2 == 'w':
                y += 1
                x -= 1
            else:
                y += 1
        else:  # E
            x += 1

    if (y, x) in black_tiles:
        black_tiles.discard((y, x))
    else:
        black_tiles.add((y, x))

print(f'Part 1: {len(black_tiles)}')

for _ in range(100):
    new_black_tiles = set()
    white_tiles = defaultdict(set)
    for tile in black_tiles:
        naybs = neighbors(tile)

        if len(black_tiles.intersection(naybs)) in [1, 2]:  # Process the black tiles
            new_black_tiles.add(tile)

        for nayb in naybs:  # Build up the dict of white tiles that are adjacent to black tiles
            if nayb not in black_tiles:
                white_tiles[nayb].add(tile)

    for w_tile, b_tiles in white_tiles.items():  # Process the white tiles
        if len(b_tiles) == 2:
            new_black_tiles.add(w_tile)

    black_tiles = new_black_tiles

print(f'Part 2: {len(new_black_tiles)}')
