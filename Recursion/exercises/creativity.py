
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


def moveDiscs(n, source, target, helper):
    if n > 0:
        moveDiscs(n-1, source, helper, target)
        target.append(source.pop())
        moveDiscs(n-1, helper, target, source)
    return target


def get_subsets(sequence):
    subsets = []
    if sequence:
        element = sequence.pop()
        subsets.append([element])
        if sequence:
            for j in get_subsets(sequence):
                subsets.append(j)
                subsets.append([element] + j)
    return subsets


def reverse_string(straight):
    if len(straight) == 1:
        return straight
    else:
        return reverse_string(straight[1:]) + straight[0]


def is_palindrome(word):
    if len(word) > 1:
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])
    else:
        return True


def has_more_vowels(word):
    vowels = ['a']
    if len(word) == 1:
        return 1 if word[0] in vowels else -1
    else:
        current = 1 if word[0] in vowels else -1
        return current + has_more_vowels(word[1:])


def sort_even_first(sequence):
    sorted_seq = []
    if len(sequence) >= 1:
        if len(sequence) > 1:
            sorted_seq = sort_even_first(sequence[1:])
        if sequence[0] % 2 == 0:
            sorted_seq.insert(0, sequence[0])
        else:
            sorted_seq.append(sequence[0])
    return sorted_seq
