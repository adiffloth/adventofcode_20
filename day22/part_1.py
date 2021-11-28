from collections import deque

def combat(winner, loser):
    winner.extend([winner.popleft(), loser.popleft()])
    return winner, loser

def score(p):
    return sum([x[0] * x[1] for x in list(zip(range(len(p), 0, -1), p))])

cards = [int(x) for x in open('day22/0.in').read().splitlines() if x.isdigit()]
p1 = deque(cards[:len(cards) // 2])
p2 = deque(cards[len(cards) // 2:])

while p1 and p2:
    if p1[0] > p2[0]:
        p1, p2 = combat(p1, p2)
    else:
        p2, p1 = combat(p2, p1)

print(max(score(p1), score(p2)))

# Tests
assert score(p1) == 32495
assert score(p2) == 0
print('Tests passed')
