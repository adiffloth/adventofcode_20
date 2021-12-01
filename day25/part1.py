# Sample
# door_pk = 17807724
# card_pk = 5764801

# Problem
door_pk = 10705932
card_pk = 12301431

def loop_size(key):
    i = 0
    x = 1
    while x != key:
        x = (x * 7) % 20201227
        i += 1
    return i

def transform(subject, loops):
    x = 1
    for i in range(loops):
        x = (x * subject) % 20201227
    return x

print(transform(card_pk, loop_size(door_pk)))
print(transform(door_pk, loop_size(card_pk)))

assert transform(card_pk, loop_size(door_pk)) == transform(door_pk, loop_size(card_pk))
