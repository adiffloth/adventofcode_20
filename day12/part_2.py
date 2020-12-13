actions = [x for x in open('day12/0.in').read().splitlines()]

dir = 90
pos = [0, 0]
wp_dx = 10
wp_dy = 1

for action in actions:
    if action[0] == 'N':
        wp_dy += int(action[1:])
    elif action[0] == 'S':
        wp_dy -= int(action[1:])
    elif action[0] == 'E':
        wp_dx += int(action[1:])
    elif action[0] == 'W':
        wp_dx -= int(action[1:])

    elif action in ['R180', 'L180']:
        wp_dx, wp_dy = -wp_dx, -wp_dy
    elif action in ['R90', 'L270']:
        wp_dx, wp_dy = wp_dy, -wp_dx
    elif action in ['L90', 'R270']:
        wp_dx, wp_dy = -wp_dy, wp_dx

    elif action[0] == 'F':
        pos[0] += wp_dx * int(action[1:])
        pos[1] += wp_dy * int(action[1:])
    print(pos)

print(abs(pos[0]) + abs(pos[1]))
