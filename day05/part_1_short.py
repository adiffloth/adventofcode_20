print(max([8 * int(s[:7].replace('F', '0').replace('B', '1'), 2) + int(s[-3:].replace('L', '0').replace('R', '1'), 2) for s in open('day05/1.in').read().splitlines()]))
