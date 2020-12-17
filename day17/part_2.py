'''
New and improved - now with 4 dimensions!
'''
from collections import defaultdict, namedtuple
from pprint import PrettyPrinter


# For a given cube, loop through all 4D neighbors and increment neighbor count.
# 3x3x3x3-1 = 80. Don't count this cube as its own neighbor.
def make_contribs(cube):
    for y in range(cube.y - 1, cube.y + 2):
        for x in range(cube.x - 1, cube.x + 2):
            for z in range(cube.z - 1, cube.z + 2):
                for w in range(cube.w - 1, cube.w + 2):
                    contribs[Cube(y, x, z, w)] += 1
    contribs[cube] -= 1  # Don't increment self.


Cube = namedtuple('Cube', ['y', 'x', 'z', 'w'])
pp = PrettyPrinter()
grid = [list(x) for x in open('day17/0.in').read().splitlines()]
active_cubes = set()

# Load initial state
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            active_cubes.add(Cube(y, x, 0, 0))

# Run cycles
cycles = 6
for cycle in range(cycles):

    # Add up contributions of every active cube
    contribs = defaultdict(int)  # {coords: neighbors}
    for cube in active_cubes:
        make_contribs(cube)

    # Apply rules to determine new set of active cubes
    next_ac = set()
    for cube, contrib in contribs.items():
        if cube in active_cubes:
            if contrib in [2, 3]:
                next_ac.add(cube)
        else:
            if contrib == 3:
                next_ac.add(cube)
    active_cubes = next_ac.copy()
    print(f'active cubes after {cycle + 1} cycles: {len(active_cubes)}')

print()
# pp.pprint(active_cubes)
print(f'Active cube final count: {len(active_cubes)}')
