'''
Appends each new item to a list and searches backwards to find the last occurence.
Simple but terribly slow.
'''
nums = [int(x) for x in open('day15/0.in').read().split(',')]
for turn in range(7, 2020):
    prev = nums[turn - 1]
    if prev in nums[:turn - 1]:
        nums.append(nums[-2::-1].index(prev) + 1)
    else:
        nums.append(0)
print(nums[-1])
