from copy import deepcopy

mask = ''
prog_mem = {}

for line in open('day14/0.in').read().splitlines():
    if line.startswith('mask'):
        mask = line.split(' = ')[1]

    else:  # 'mem'
        line_parts = line.split(' = ')
        addr = bin(int(line_parts[0][4:-1]))[2:].zfill(36)
        val = int(line_parts[1])
        new_addr = ''
        for addr_c, mask_c in zip(addr, mask):
            new_addr += addr_c if mask_c == '0' else '1' if mask_c == '1' else 'X'

        addr_locs = [[]]
        for char in new_addr:
            if char in ['0', '1']:
                for addr_loc in addr_locs:
                    addr_loc.append(char)
            else:  # 'X' - duplicate all existing address fragments, add '1' to half, '2' to the other half
                addr_locs.extend(deepcopy(addr_locs))
                for i, addr_loc in enumerate(addr_locs):
                    addr_loc.append('0' if (i < len(addr_locs) / 2) else '1')

        for addr_loc in addr_locs:
            prog_mem[''.join(addr_loc)] = val

print(f'Answer: {sum(prog_mem.values())}')
