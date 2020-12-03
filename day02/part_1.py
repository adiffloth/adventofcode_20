lines = [x for x in open('day02/1.in').read().splitlines()]

ans = 0

for line in lines:
    counts, char, passwd = line.split()
    gt, lt = [int(i) for i in counts.split('-')]
    print(lt, passwd.count(char), gt, char[0])
    if gt <= passwd.count(char[0]) <= lt:
        ans += 1

print(ans)
