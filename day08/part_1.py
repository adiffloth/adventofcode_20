instrs = [x.split() for x in open('day08/1.in').read().splitlines()]

ptr = 0
acc = 0
visited = set()
while ptr < len(instrs):
    op, arg = instrs[ptr][0], int(instrs[ptr][1])

    if op == 'acc':
        acc += arg
        ptr += 1
    elif op == 'jmp':
        ptr += arg
    elif op == 'nop':
        ptr += 1

    if ptr in visited:
        print(acc)
        break
    else:
        visited.add(ptr)
