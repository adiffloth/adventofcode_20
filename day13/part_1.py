lines = [x for x in open('day13/0.in').read().splitlines()]
time = int(lines[0])
buses = lines[1].split(',')
bi = [int(x) for x in buses if x != 'x']

# print(bi)
gaps = {}
for i in bi:
    # print(i - (time % i))
    gaps[i] = i - (time % i)

best_bus = min(gaps, key=gaps.get)
print(gaps[best_bus] * best_bus)
