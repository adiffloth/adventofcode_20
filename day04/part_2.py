import re

lines = [x for x in open('day04/1.in').read().splitlines()]
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

p_count = 0
l_count = 0
passports = ['']
for line in lines:
    l_count += 1
    if line == '':
        passports.append(line)
        p_count += 1
    else:
        passports[p_count] = passports[p_count] + ' ' + line

valid_p = 0
for p_line in passports:
    if sum([x in p_line for x in fields]) != 7:
        continue

    p_data = {}
    pfs = p_line.split()
    for pf in pfs:
        k, v = pf.split(':')
        p_data[k] = v

    if not (1920 <= int(p_data['byr']) <= 2002):
        continue

    if not (2010 <= int(p_data['iyr']) <= 2020):
        continue

    if not (2020 <= int(p_data['eyr']) <= 2030):
        continue

    if p_data['hgt'][-2:] == 'cm':
        if not (150 <= int(p_data['hgt'][:-2]) <= 193):
            continue
    elif p_data['hgt'][-2:] == 'in':
        if not (59 <= int(p_data['hgt'][:-2]) <= 76):
            continue
    else:
        continue

    if not (re.match(r'^#[a-z0-9]{6}$', p_data['hcl'])):
        continue

    if not (p_data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        continue

    if not (re.match(r'^[0-9]{9}$', p_data['pid'])):
        continue

    valid_p += 1

print(valid_p)
