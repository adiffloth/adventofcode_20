import re

s = '#b6652a'
s1 = 'a9'
s2 = '#6'

if re.match(r'^#[a-z0-9]{6}$', s):
    print('valid')
else:
    print('invalid')


if re.match(r'^#[0-9]$', s2):
    print('valid')
else:
    print('invalid')
