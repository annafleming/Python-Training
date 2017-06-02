from random import randrange

def is_multiple(n, m):
    return n % m == 0


def is_even(n):
    while n >= 2:
        n -= 2
    return False if n == 1 else True


def minmax(data):
    min_item = max_item = data[0]
    for item in data:
        if item < min_item:
            min_item = item
        if item > max_item:
            max_item = item
    return min_item, max_item


def get_sum_of_squares(n):
    return sum([i**2 for i in range(n)])


def get_sum_of_squares_of_odd_numbers(n):
    return sum([i ** 2 for i in range(n) if i % 2 == 1])


def get_rand_element(seq):
    return seq[randrange(0, len(seq) - 1, 1)]

