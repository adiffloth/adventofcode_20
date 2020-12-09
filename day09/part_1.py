lines = [int(x) for x in open('day09/0.in').read().splitlines()]

pre_len = 25  # CHANGE ME: test=5, prod=25
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
        print(lines[i])
        break
