import re

# rules_lst, msgs = open('day19/1.in').read().split('\n\n')

rules, lines = open('day19/0.in').read().split('\n\n')
print(type(rules), type(lines))

rules_s = {}
for line in rules.splitlines():
    k, _, v = line.partition(': ')
    rules_s[k] = v


def _get_re(s: str) -> str:
    if s == '|':
        return s

    rule_s = rules_s[s]
    if rule_s.startswith('"'):
        return rule_s.strip('"')
    else:
        return f'({"".join(_get_re(part) for part in rule_s.split())})'


ret = re.compile(_get_re('0'))

print(sum(bool(ret.fullmatch(line)) for line in lines.splitlines()))
