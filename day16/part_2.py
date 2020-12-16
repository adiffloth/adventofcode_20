'''
Now we need to figure out which field is which through process of elimination,
so we need to keep track of invdividual rules with a dict.
'''
from collections import defaultdict


# For a list of values, which rules are candidates?
def rules_include(list_i):
    matched_rules = set()
    if type(list_i) == int:
        list_i = [list_i]
    for rule_id, rule in rules_d.items():
        include = True
        for i in list_i:
            if i not in rule[0] and i not in rule[1]:
                include = False
        if include:
            matched_rules.add(rule_id)
    return matched_rules


# Parse input data
lines = [x for x in open('day16/0.in').read().splitlines()]
mt_line = lines.index('your ticket:')
nt_line = lines.index('nearby tickets:')
rules = [x for x in lines[:mt_line - 1]]
my_ticket = lines[mt_line + 1]
nearby_tix = [x for x in lines[nt_line + 1:]]

# Build rule dict and set
rules_d = defaultdict(list)
rule_values = set()  # For part 1
for rule_id, rule in enumerate(rules):
    r1_lo = int(rule.split()[-3].split('-')[0])
    r1_hi = int(rule.split()[-3].split('-')[1])
    r2_lo = int(rule.split()[-1].split('-')[0])
    r2_hi = int(rule.split()[-1].split('-')[1])

    rules_d[rule_id].append(range(r1_lo, r1_hi + 1))
    rules_d[rule_id].append(range(r2_lo, r2_hi + 1))
    rule_values.update(range(r1_lo, r1_hi + 1))
    rule_values.update(range(r2_lo, r2_hi + 1))

# Part 1 - Get the valid tickets
valid_tix = []
for ticket in nearby_tix:
    ticket_vals = [int(x) for x in ticket.split(',')]
    valid = True
    for i in ticket_vals:
        if i not in rule_values:
            valid = False
            break
    if valid:
        valid_tix.append(ticket_vals)

# Part 2 - Figure out the fields
# Build dict of field values from valid tickets
fields = defaultdict(list)
for tic in valid_tix:
    for field_num, field_val in enumerate(tic):
        fields[field_num].append(field_val)

field_candidates = {}  # Candidates for fields still to be resolved
fields_resolved = {}  # Fields already resolved

# First pass at resolving fields
for field_id, field in fields.items():
    field_candidates[field_id] = rules_include(field)

while field_candidates:  # Still have unresolved fields
    # If any fields are down to one candidate, move it to resolved
    for id, candidates in field_candidates.items():
        if len(candidates) == 1:
            fields_resolved[id] = candidates.pop()

    # Remove resolved fields from field list AND rules list
    for field_id, rule_id in fields_resolved.items():
        fields.pop(field_id, '')
        rules_d.pop(rule_id, '')

    # Rebuild candidate list to see if reduced field and rule sets
    # allow us to resolve another field.
    field_candidates = {}
    for field_id, field in fields.items():
        field_candidates[field_id] = rules_include(field)

# Need to look up position by field not the reverse
reverse_lookup = {}
for k, v in fields_resolved.items():
    reverse_lookup[v] = k

# Grab the values of the departure* fields from my ticket and multipy.
product = 1
for id, rule in enumerate(rules):
    if rule.startswith('departure'):
        product *= int(my_ticket.split(',')[reverse_lookup[id]])
print(product)
