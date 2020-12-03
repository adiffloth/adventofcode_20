import math

lines = [x for x in open('day03/1.in').read().splitlines()]

num_lines = len(lines)
single_wide = len(lines[0])
num_reps = math.ceil(num_lines * 3 / single_wide)

full_map = []
for line in lines:
    full_map.append(line * num_reps)

count = 0
for i, line in enumerate(full_map):
    if line[i * 3] == '#':
        count += 1

print(count)
