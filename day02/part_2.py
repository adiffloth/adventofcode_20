lines = [x for x in open('day02/1.in').read().splitlines()]

ans = 0

for line in lines:
    counts, char, passwd = line.split()
    gt, lt = [int(i) for i in counts.split('-')]
    # print(gt, lt, char, passwd, len(passwd))
    if (passwd[gt - 1] == char[0]) != (passwd[lt - 1] == char[0]):
        ans += 1

print(ans)
