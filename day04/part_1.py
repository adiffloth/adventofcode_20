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

    valid_p += 1

print(valid_p)
