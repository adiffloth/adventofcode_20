'''
For Part 1, only care if a ticket has a value that doesn't match ANY rule.
Don't need to track which specific rules match, so just use a set.
'''

lines = [x for x in open('day16/0.in').read().splitlines()]
mt_line = lines.index('your ticket:')
nt_line = lines.index('nearby tickets:')
rules = [x for x in lines[:mt_line - 1]]
my_ticket = lines[mt_line + 1]
nearby_tix = [x for x in lines[nt_line + 1:]]

rule_values = set()
for rule in rules:
    r1_lo = int(rule.split()[-3].split('-')[0])
    r1_hi = int(rule.split()[-3].split('-')[1])
    r2_lo = int(rule.split()[-1].split('-')[0])
    r2_hi = int(rule.split()[-1].split('-')[1])

    rule_values.update(range(r1_lo, r1_hi + 1))
    rule_values.update(range(r2_lo, r2_hi + 1))

invalid_vals = []
for ticket in nearby_tix:
    ticket_vals = [int(x) for x in ticket.split(',')]
    for i in ticket_vals:
        if i not in rule_values:
            invalid_vals.append(i)

print(sum(invalid_vals))
