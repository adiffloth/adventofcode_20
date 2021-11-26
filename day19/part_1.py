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

# Build re pattern, starting with rule 0
ptrn = re.compile(build_re('0'))
match_count = 0

# Count the messages that match the re
for msg in msgs:
    # print(msg, ptrn.fullmatch(msg))
    if ptrn.fullmatch(msg):
        match_count += 1

print(match_count)
