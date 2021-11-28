from collections import deque
from itertools import islice

def recursive_combat(p1, p2):
    prev_hands = set()
    while p1 and p2:
        if (str(p1), str(p2)) in prev_hands:  # Check for recursion loops
            return True, p1, p2
        prev_hands.add((str(p1), str(p2)))

        c1 = p1.popleft()
        c2 = p2.popleft()

        if (c1 <= len(p1)) and (c2 <= len(p2)):  # We have enough cards to play another round
            p1_wins, _, _ = recursive_combat(deque(islice(p1, c1)), deque(islice(p2, c2)))
        else:  # Not enough cards to keep playing, determine a winner
            p1_wins = c1 > c2

        if p1_wins:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return p1_wins, p1, p2

def score(p):
    return sum([x[0] * x[1] for x in list(zip(range(len(p), 0, -1), p))])

cards = [int(x) for x in open('day22/0.in').read().splitlines() if x.isdigit()]
p1 = deque(cards[:len(cards) // 2])
p2 = deque(cards[len(cards) // 2:])

_, p1, p2 = recursive_combat(p1, p2)

print(max(score(p1), score(p2)))

# Tests
assert score(p1) == 32665
assert score(p2) == 0
print('Tests passed')
