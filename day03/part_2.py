import math
# import sys

lines = [x for x in open('day03/1.in').read().splitlines()]
num_lines = len(lines)
single_wide = len(lines[0])


def tree_finder(dx, dy):
    num_reps = math.ceil(num_lines * dx / single_wide)

    full_map = []
    for line in lines:
        full_map.append(line * num_reps)

    print(f'y: {len(full_map)}')
    print(f'x: {len(full_map[0])}')

    count = 0
    for i in range(int(len(full_map) / dy)):

        if full_map[i * dy][int(i * dx)] == '#':
            count += 1

    print(count)
    return(count)


t1 = tree_finder(1, 1)
t2 = tree_finder(3, 1)
t3 = tree_finder(5, 1)
t4 = tree_finder(7, 1)
t5 = tree_finder(1, 2)

print(t1 * t2 * t3 * t4 * t5)
