def get_row(s):
    return int(s[:7].replace('F', '0').replace('B', '1'), 2)


def get_col(s):
    return int(s[-3:].replace('L', '0').replace('R', '1'), 2)


def get_seat_id(s):
    return 8 * get_row(s) + get_col(s)


seats_b = [x for x in open('day05/1.in').read().splitlines()]
print(max(get_seat_id(x) for x in seats_b))
