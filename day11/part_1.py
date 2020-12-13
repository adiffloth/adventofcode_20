import pprint
import copy

TOLERANCE = 4


def sum_adj(r, c):
    row_min = max(0, r - 1)
    row_max = min(r + 1, len(plane) - 1)
    col_min = max(0, c - 1)
    col_max = min(c + 1, len(plane[0]) - 1)

    count = 0
    for rr in range(row_min, row_max + 1):
        for cc in range(col_min, col_max + 1):
            count += plane[rr][cc] == '#'
    count -= plane[r][c] == '#'
    return count


def choose_seat(r, c):
    if plane[r][c] == 'L' and sum_adj(r, c) == 0:
        return '#'
    if plane[r][c] == '#' and sum_adj(r, c) >= TOLERANCE:
        return 'L'
    else:
        return plane[r][c]


def update():
    new_plane = []
    for row in range(len(plane)):
        new_row = ''
        for col in range(len(plane[0])):
            new_row += choose_seat(row, col)
        new_plane.append(new_row)
    return new_plane


pp = pprint.PrettyPrinter()
plane = [x for x in open('day11/0.in').read().splitlines()]
prev_plane = []
while prev_plane != plane:
    prev_plane = copy.deepcopy(plane)
    plane = update()

print(''.join(plane).count('#'))
