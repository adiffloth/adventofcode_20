with open('day01/1.in') as f:
    nums = [int(line.rstrip('\n')) for line in f]

nums.sort()
for i, first in enumerate(nums):
    for second in nums[i + 1:]:
        if first + second == 2020:
            print(f'{first * second}')
        if first + second > 2020:
            break
