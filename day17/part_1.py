'''
Unlike Day 11, space is not confined, so we don't have to worry about stepping
outside the bounds of the arrays. No max(0, blah) nonsense, just grab +/-1
in every dimension to get the neighbors.

Since space is now infinite, we can no longer track every coordinate's state.
Where we used to loop through every coord and count its neighbors to determine
its own state, now we only track active coords and loop through those to
accumulate contributions to its neighboring points' neighbor counts. When all
the contributions are done, loop through them to apply active/inactive logic.
'''
from collections import defaultdict, namedtuple
from pprint import PrettyPrinter


# For a given cube, loop through all 3D neighbors and increment neighbor count.
# 3x3x3-1 = 26. Don't count this cube as its own neighbor.
def make_contribs(cube):
    for y in range(cube.y - 1, cube.y + 2):
        for x in range(cube.x - 1, cube.x + 2):
            for z in range(cube.z - 1, cube.z + 2):
                contribs[Cube(y, x, z)] += 1
    contribs[cube] -= 1  # Don't increment self.


Cube = namedtuple('Cube', ['y', 'x', 'z'])
pp = PrettyPrinter()
grid = [list(x) for x in open('day17/0.in').read().splitlines()]
active_cubes = set()

# Load initial state
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            active_cubes.add(Cube(y, x, 0))

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
