prod = True
if prod:
    lines = [int(x) for x in open('day09/0.in').read().splitlines()]
    pre_len = 25
else:
    lines = [int(x) for x in open('day09/1.in').read().splitlines()]
    pre_len = 5

target = None
for i in range(pre_len, len(lines)):
    found = False
    for j in range(i - pre_len, i):
        for k in range(j + 1, i):
            if lines[k] + lines[j] == lines[i]:
                found = True
                break
        if found:
            break
    if not found:
        target = lines[i]
        break

print(f'Part 1 target: {target}')

pt2_ans = None
for i in range(len(lines)):
    total = lines[i]
    for j in range(i + 1, len(lines)):
        total += lines[j]
        if total == target:
            pt2_ans = min(lines[i:j]) + max(lines[i:j])
            break
    if pt2_ans:
        break

print(f'Part 2 answer: {pt2_ans}')
