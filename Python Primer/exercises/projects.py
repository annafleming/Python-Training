
def make_change(charged, given):
    bills = [100, 50, 20, 10, 5, 1]
    change = []
    left = given - charged
    for bill in bills:
        if not left:
            break
        while left >= bill:
            change.append(bill)
            left -= bill
    return change


def make_change_with_generator(charged, given):
    return [i for i in _change_generator(charged, given)]


def _change_generator(charged, given):
    bills = [100, 50, 20, 10, 5, 1]
    left = given - charged
    for bill in bills:
        if not left:
            break
        while left >= bill:
            yield bill
            left -= bill