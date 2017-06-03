
def reverse_list(list_of_ints):
    return [list_of_ints[len(list_of_ints) - i - 1] for i in range(len(list_of_ints))]


def has_product_odd(sequence):
    for i in sequence:
        for j in sequence:
            if j * i % 2 == 1 and i != j:
                return True
    return False


def are_numbers_unique(sequence):
    return len(set(sequence)) == len(sequence)

