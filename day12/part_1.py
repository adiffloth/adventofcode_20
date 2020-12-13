actions = [x for x in open('day12/0.in').read().splitlines()]

dir = 90
pos = [0, 0]

for action in actions:
    if action[0] == 'N':
        pos[1] += int(action[1:])
    elif action[0] == 'S':
        pos[1] -= int(action[1:])
    elif action[0] == 'E':
        pos[0] += int(action[1:])
    elif action[0] == 'W':
        pos[0] -= int(action[1:])
    elif action[0] == 'R':
        dir = (dir + int(action[1:])) % 360
    elif action[0] == 'L':
        dir = (dir - int(action[1:])) % 360
    elif action[0] == 'F':
        if dir == 0:
            pos[1] += int(action[1:])
        elif dir == 180:
            pos[1] -= int(action[1:])
        elif dir == 90:
            pos[0] += int(action[1:])
        elif dir == 270:
            pos[0] -= int(action[1:])
    print(pos)

print(abs(pos[0]) + abs(pos[1]))
