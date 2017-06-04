from random import randint
import string
import re

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


def shuffle(sequence):
    sequence = sequence[:]
    sequence_len = len(sequence)
    shuffled = []
    for i in range(sequence_len):
        rand_position = randint(0, len(sequence) - 1)
        shuffled.append(sequence[rand_position])
        del sequence[rand_position]
    return shuffled


def get_dot_product(seq1, seq2):
    return [seq1[i] * seq2[i] for i in range(len(seq1))]


def insert_element_by_index(sequence, index, value):
    try:
        sequence[index] = value
    except IndexError:
        return "Don’t try buffer overflow attacks in Python!"


def count_vowels(text):
    vowel = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowel:
            count += 1
    return count


def remove_punctuation(sentence):
    return re.sub('['+str(string.punctuation)+']', '', sentence)

