import pprint
import queue
q = queue.Queue()

pp = pprint.PrettyPrinter()

lines = [x for x in open('day07/2.in').read().splitlines()]

bags = {}
for line in lines:
    bag, contents = line.split('contain')
    contents = contents.replace('bags', '').replace('bag', '').replace('.', '')
    # contents = [s[3:].rstrip() for s in contents.split(',')]
    contents = [None if 'other' in s else s[3:].rstrip() for s in contents.split(',')]
    bags[bag[:-6]] = contents

# pp.pprint(bags)


def get_parents(b):
    parents = []
    for bag, contents in bags.items():
        if b in contents:
            parents.append(bag)
    return parents


possibles = set()
q = set()
q.add('shiny gold')

while q:
    parents = get_parents(q.pop())
    for parent in parents:
        if parent not in possibles:
            q.add(parent)
        possibles.add(parent)

# pp.pprint(possibles)
print(len(possibles))
