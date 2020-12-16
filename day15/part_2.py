'''
Uses a dict instead of a list. Only stores the last time a number was spoken.
Much faster on lookups, uses less space, but doesn't keep the full history.
'''
nums_d = {}

for i, num in enumerate(open('day15/0.in').read().split(',')[:-1]):
    nums_d[int(num)] = i
min, max = len(nums_d), 30000000
next = int(open('day15/0.in').read().split(',')[-1])

prev = 0
for turn in range(min, max):
    prev = next
    if next in nums_d:
        dist = turn - nums_d[next]
        nums_d[next] = turn
        next = dist
    else:
        nums_d[next] = turn
        next = 0
print(prev)
