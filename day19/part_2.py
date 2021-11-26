import re


# Process each rule by recursively substituting the references to other rules
def build_re(rule_id):

    rule = rules.get(rule_id)

    # Base cases
    if rule.strip('"') == ('a'):
        return 'a'
    if rule.strip('"') == ('b'):
        return 'b'

    # Recursive case
    s = "".join('|' if part == '|' else build_re(part) for part in rule.split())
    return f'({s})'


# Build dict of rules
rules_lst, msgs = map(str.splitlines, open('day19/0.in').read().split('\n\n'))
rules = {}
for rule in rules_lst:
    rule_id, rule_text = rule.split(': ')
    rules[rule_id] = rule_text

ptrn_31 = re.compile(build_re('31'))
ptrn_42 = re.compile(build_re('42'))

match_count = 0
for msg in msgs:
    pos = 0

    cnt_42 = 0
    match = ptrn_42.match(msg, pos)
    while match:
        cnt_42 += 1
        pos = match.end()
        match = ptrn_42.match(msg, pos)

    cnt_31 = 0
    match = ptrn_31.match(msg, pos)
    while match:
        cnt_31 += 1
        pos = match.end()
        match = ptrn_31.match(msg, pos)

    if pos == len(msg) and 0 < cnt_31 < cnt_42:
        match_count += 1

print(match_count)
