groups = [x for x in open('day06/1.in').read().splitlines()]
print(len(groups))

counts = []
group_responses = []
for responses in groups:
    if responses == '':
        counts.append(len(set.intersection(*group_responses)))
        group_responses = []
    else:
        group_responses.append(set(list(responses)))

print(sum(counts))
