def test_run(test_prog):

    ptr = 0
    acc = 0
    cyclic = False
    visited = [0]
    while ptr < len(test_prog):
        op, arg = test_prog[ptr][0], int(test_prog[ptr][1])
        if op == 'acc':
            acc += arg
            ptr += 1
        elif op == 'jmp':
            ptr += arg
        elif op == 'nop':
            ptr += 1

        if ptr in visited:
            cyclic = True
            break
        else:
            visited.append(ptr)
    return acc, visited, cyclic


# Run the unchanged instructions first.
instrs = [x.split() for x in open('day08/1.in').read().splitlines()]
acc, visited, cyclic = test_run(instrs)

# Build a list of all the jmp and nop operations we actually executed.
candidates = set()
for v in visited:
    if instrs[v][0][:3] in ['jmp', 'nop']:
        candidates.add(v)

# Swap jmp and nop until a program executes without looping.
for c in candidates:
    test_prog = [x.split() for x in open('day08/1.in').read().splitlines()]
    if test_prog[c][0] == 'jmp':
        test_prog[c][0] = 'nop'
    else:
        test_prog[c][0] = 'jmp'
    acc, visited, cyclic = test_run(test_prog)
    if not cyclic:
        print(c, acc)
        break
