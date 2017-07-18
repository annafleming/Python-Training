
def populate_linked_list(ll, items):
    for item in items:
        ll.enqueue(item)
    return ll


def get_second_to_last(ll):
    for index, element in enumerate(ll):
        if index == len(ll) - 2:
            return element


def concatenate_linked_lists(L, M):
    C = L
    for element in M:
        C.enqueue(element)
    return C


def recursively_count_nodes(L):
    return L._count_nodes(L.get_first_node())






