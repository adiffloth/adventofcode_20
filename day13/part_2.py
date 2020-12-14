'''
Wouldn't have gotten this on my own.

Credit to Joel Grus' video on YouTube for making me aware of Chinese Remainder Theorem:
https://www.youtube.com/watch?v=W8IBqBSsYKg

Adapted chinese_remainder() and mul_inv() from:
https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
'''

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


lines = [x for x in open('day13/0.in').read().splitlines()][1].split(',')
buses = []
for i, bus in enumerate(lines):
    if bus != 'x':
        buses.append((int(bus), i, (int(bus) - i) % int(bus)))
print(buses)
# Each tuple is: bus time, offset from first bus, remainder at first bus time.
# Feed bus time and remainders into the CRT code.

n = [b[0] for b in buses]
a = [b[2] for b in buses]

ans = chinese_remainder(n, a)

# Check answer against expected remainders
for bus in buses:
    assert bus[2] == ans % bus[0]
print('All tests pass.')
print(f'Answer: {ans}')
