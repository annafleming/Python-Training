
def in_list(sequence, item):
    return binary_search(sequence, item, 0, len(sequence) - 1)


def binary_search(data, target, low, high):
    mid = (high + low) // 2
    if low > high:
        return False
    if target == data[mid]:
        return True
    if target < data[mid]:
        return binary_search(data, target, low, mid-1)
    else:
        return binary_search(data, target, mid+1, high)
