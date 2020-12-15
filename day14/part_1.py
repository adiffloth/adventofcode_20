lines = [x for x in open('day14/0.in').read().splitlines()]
prog_mem = {}
zeros_mask = ones_mask = ''

for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
        zeros_mask = int(''.join(['0' if c == '0' else '1' for c in mask]), 2)
        ones_mask = int(''.join(['1' if c == '1' else '0' for c in mask]), 2)
    else:
        line_parts = line.split(' = ')
        mem_write = [int(line_parts[0][4:-1]), int(line_parts[1])]
        mem_write[1] = mem_write[1] & zeros_mask
        mem_write[1] = mem_write[1] | ones_mask
        prog_mem[mem_write[0]] = mem_write[1]

print(f'Answer: {sum(prog_mem.values())}')
