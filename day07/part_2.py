import pprint

pp = pprint.PrettyPrinter()
lines = [x for x in open('day07/2.in').read().splitlines()]
bags = {}
for line in lines:
    bag, contents = line.split('contain')
    contents = contents.replace('bags', '').replace('bag', '').replace('.', '')
    contents = [None if 'other' in s else [s[3:].rstrip()] * int(s[1]) for s in contents.split(',')]
    bags[bag[:-6]] = [item for sublist in contents for item in sublist] if contents[0] else [None]
# pp.pprint(bags)

collection_of_bags = []  # TODO: replace with count
q = ['shiny gold']

while q:
    curr_bag = q.pop()
    if curr_bag:
        children = bags[curr_bag]
        for child in children:
            if child:
                collection_of_bags.append(child)
                q.append(child)

# pp.pprint(collection_of_bags)
print(len(collection_of_bags))
