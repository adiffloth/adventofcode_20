lines = [int(x) for x in open('day10/0.in').read().splitlines()]
lines = lines + [0] + [max(lines) + 3]
lines.sort()

jolt_1 = jolt_3 = 0
for i in range(len(lines) - 1):
    if lines[i + 1] - lines[i] == 1:
        jolt_1 += 1
    else:
        jolt_3 += 1

print((jolt_1) * (jolt_3))
