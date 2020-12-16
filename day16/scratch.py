rules = {
    0: [range(0, 10), range(20, 30)],
    1: [range(70, 80), range(90, 100)],
    2: [range(50, 75), range(95, 110)],
    3: [range(5000, 10000), range(0, 5)],
    4: [range(50, 75), range(72, 74)]
}


def rule_match(list_i):
    matched_rules = set()
    if type(list_i) == int:
        list_i = [list_i]
    for i in list_i:
        for rule_id, rule in rules.items():
            for rng in rule:
                matched_rules.add(rule_id) if i in rng else False
    return matched_rules


assert rule_match(25) == {0}
assert rule_match(2) == {0, 3}
assert rule_match(15) == set()
assert rule_match(73) == {1, 2, 4}
assert rule_match([8, 7000]) == {0, 3}
print('Tests passed')

rule_values = set()
for rule in rules.values():
    for rng in rule:
        rule_values.update(rng)

assert 5 in rule_values
assert 50000 not in rule_values
assert 93 in rule_values
assert 99 in rule_values
print('Tests passed')


def rule_exclude(list_i):
    matched_rules = set()
    if type(list_i) == int:
        list_i = [list_i]

    for rule_id, rule in rules.items():
        include = True

        for i in list_i:
            if i not in rule[0] and i not in rule[1]:
                include = False

        if include:
            matched_rules.add(rule_id)
    return matched_rules


rules = {
    0: [range(0, 2), range(4, 20)],
    1: [range(0, 6), range(8, 20)],
    2: [range(0, 14), range(16, 20)]
}

fields = {
    0: [3, 15, 5],
    1: [9, 1, 14],
    2: [18, 5, 9]
}

field_candidates = {}
fields_resolved = {}

for field_id, field in fields.items():
    field_candidates[field_id] = rule_exclude(field)

while field_candidates:

    # print(f'Candidates pre:  {field_candidates}')
    for id, candidates in field_candidates.items():
        if len(candidates) == 1:
            fields_resolved[id] = candidates.pop()
    # print(f'Resolved: {fields_resolved}')

    for field_id, rule_id in fields_resolved.items():
        fields.pop(field_id, '')
        rules.pop(rule_id, '')

    field_candidates = {}
    for field_id, field in fields.items():
        field_candidates[field_id] = rule_exclude(field)
    # print(f'Candidates post: {field_candidates}')
    # print()

print()
print(f'Final:  {fields_resolved}')
ans = {0: 1, 1: 0, 2: 2}
print(f'Answer: {ans}')
assert fields_resolved == ans
print('Tests passed')
