
def get_min_max(sequence, min=None, max=None):
    if min is None:
        min = sequence[0]
    if max is None:
        max = sequence[0]
    if len(sequence) == 0:
        return min, max
    else:
        min = min if sequence[0] > min else sequence[0]
        max = max if sequence[0] < max else sequence[0]
        return get_min_max(sequence[1:], min, max)
