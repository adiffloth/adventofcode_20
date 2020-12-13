lines = [int(x) for x in open('day10/0.in').read().splitlines()]
lines = lines + [0] + [max(lines) + 3]
lines.sort()

paths = {lines[0]: 1}
for x in lines[1:]:
    paths[x] = sum(paths[x - y] for y in range(1, 4) if x - y in paths)

print(paths[lines[-1]])
