
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