
def get_min_max(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    if len(sequence) == 2:
        return sequence[0], sequence[1] if sequence[0] < sequence[1] else sequence[1], sequence[0]
    mid = len(sequence) // 2
    min_max_1 = get_min_max(sequence[:mid])
    min_max_2 = get_min_max(sequence[mid:])
    comb_min = min_max_1[0] if min_max_1[0] < min_max_2[0] else min_max_2[0]
    comb_max = min_max_1[1] if min_max_1[1] > min_max_2[1] else min_max_2[1]
    return comb_min, comb_max
