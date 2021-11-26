import re

rules, lines = map(str.splitlines, open('day19/0.in').read().split('\n\n'))

rules_s = {}
for line in rules:
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

print(sum(bool(ret.fullmatch(line)) for line in lines))
