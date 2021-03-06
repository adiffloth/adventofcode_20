def get_row(s):
    return int(s[:7].replace('F', '0').replace('B', '1'), 2)


def get_col(s):
    return int(s[-3:].replace('L', '0').replace('R', '1'), 2)


def get_seat_id(s):
    return 8 * get_row(s) + get_col(s)


seats_b = [x for x in open('day05/1.in').read().splitlines()]
seat_ids = [get_seat_id(x) for x in seats_b]
seat_ids.sort()

for i, _ in enumerate(seat_ids):
    if seat_ids[i] != seat_ids[i + 1] - 1:
        print(seat_ids[i] + 1)
        break  # Also avoids off-by-one error at the end.
