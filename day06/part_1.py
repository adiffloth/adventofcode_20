groups = [x for x in open('day06/1.in').read().splitlines()]
print(len(groups))

counts = []
uniques = set()
for responses in groups:
    if responses == '':
        counts.append(len(uniques))
        uniques.clear()
    else:
        for response in responses:
            uniques.add(response)

print(sum(counts))
