import sys
with open('day01/1.in') as f:
    nums = [int(line.rstrip('\n')) for line in f]

nums.sort()
for i, first in enumerate(nums):
    for j, second in enumerate(nums[i + 1:]):
        for third in nums[i + 2:]:
            if first + second + third == 2020:
                print(f'{first * second * third}')
                sys.exit(0)
            if first + second + third > 2020:
                break
