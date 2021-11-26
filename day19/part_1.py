import re

rules_lst, msgs = map(str.splitlines, open('day19/0.in').read().split('\n\n'))
rules = {}
for rule in rules_lst:
    rule_id, rule_text = rule.split(': ')
    rules[rule_id] = rule_text


def build_re(s):
    if s == '|':
        return '|'

    rule = rules[s]
    if rule.startswith('"'):
        return rule.strip('"')
    else:
        return f'({"".join(build_re(part) for part in rule.split())})'


ptrn = re.compile(build_re('0'))
match_count = 0

for msg in msgs:
    # print(msg, ptrn.fullmatch(msg))
    if ptrn.fullmatch(msg):
        match_count += 1

print(match_count)
