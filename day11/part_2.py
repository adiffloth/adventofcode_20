import pprint
import copy

TOLERANCE = 5


def sum_viz(r, c):
    count = 0

    # up
    r1 = r - 1
    while (0 <= r1 <= len(plane) - 1):
        if plane[r1][c] != '.':
            count += plane[r1][c] == '#'
            break
        r1 -= 1

    # down
    r1 = r + 1
    while (0 <= r1 <= len(plane) - 1):
        if plane[r1][c] != '.':
            count += plane[r1][c] == '#'
            break
        r1 += 1

    # left
    c1 = c - 1
    while (0 <= c1 <= len(plane[0]) - 1):
        if plane[r][c1] != '.':
            count += plane[r][c1] == '#'
            break
        c1 -= 1

    # right
    c1 = c + 1
    while (0 <= c1 <= len(plane[0]) - 1):
        if plane[r][c1] != '.':
            count += plane[r][c1] == '#'
            break
        c1 += 1

    # down right
    r1, c1 = r + 1, c + 1
    while (0 <= r1 <= len(plane) - 1) and (0 <= c1 <= len(plane[0]) - 1):
        if plane[r1][c1] != '.':
            count += plane[r1][c1] == '#'
            break
        r1 += 1
        c1 += 1

    # down left
    r1, c1 = r + 1, c - 1
    while (0 <= r1 <= len(plane) - 1) and (0 <= c1 <= len(plane[0]) - 1):
        if plane[r1][c1] != '.':
            count += plane[r1][c1] == '#'
            break
        r1 += 1
        c1 -= 1

    # up right
    r1, c1 = r - 1, c + 1
    while (0 <= r1 <= len(plane) - 1) and (0 <= c1 <= len(plane[0]) - 1):
        if plane[r1][c1] != '.':
            count += plane[r1][c1] == '#'
            break
        r1 -= 1
        c1 += 1

    # up left
    r1, c1 = r - 1, c - 1
    while (0 <= r1 <= len(plane) - 1) and (0 <= c1 <= len(plane[0]) - 1):
        if plane[r1][c1] != '.':
            count += plane[r1][c1] == '#'
            break
        r1 -= 1
        c1 -= 1

    return count


def choose_seat(r, c):
    if plane[r][c] == 'L' and sum_viz(r, c) == 0:
        return '#'
    if plane[r][c] == '#' and sum_viz(r, c) >= TOLERANCE:
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
