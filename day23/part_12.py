class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, value):
        new_node = Node(value, self.next)
        new_node.next = self.next
        self.next = new_node
        return new_node

    def pickup_3(self):
        cut = self.next
        self.next = self.next.next.next.next
        return cut

    def insert_3(self, cut):
        cut.next.next.next = self.next
        self.next = cut

    def __repr__(self):
        return(f'{self.value}->{self.next.value if self.next else None}')


# INPUT = '389125467'  # Sample
INPUT = '784235916'  # To solve

is_part_1 = False
num_cups = 9 if is_part_1 else 1_000_000
num_turns = 100 if is_part_1 else 10_000_000

cups = {}
cups_ls = [int(x) for x in INPUT]
cups_ls.extend(range(max(cups_ls) + 1, num_cups + 1))  # Extend to 1m for Part 2
min_cup = min(cups_ls)
max_cup = max(cups_ls)

cups[cups_ls[0]] = current = Node(cups_ls[0])  # Load the linked list with nodes
for i in cups_ls[1:]:
    cups[i] = current = current.insert(i)
current.next = cups[cups_ls[0]]  # Link the last node back to the first one

current = current.next  # Start at the first cup
for i in range(num_turns):
    cut = current.pickup_3()
    dest = cups[current.value - 1] if current.value > 1 else cups[max_cup]  # Get next deest, check for wrap around
    while dest.value in [cut.value, cut.next.value, cut.next.next.value]:  # Is dest in the 3 cups we picked?
        dest = cups[dest.value - 1] if dest.value > 1 else cups[max_cup]
    dest.insert_3(cut)  # Place the 3 picked up cups at the destination
    current = current.next

current = cups[1].next

if is_part_1:
    for _ in range(num_cups - 1):
        print(current.value, end='')
        current = current.next
    print()
else:
    print(current.value * current.next.value)
