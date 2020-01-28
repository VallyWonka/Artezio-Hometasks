"""
Hometasks from Lesson One
"""


def capitalise_names(name):
    """
    Prints a correctly capitalised name
    """
    name = name.split()
    for ind, word in enumerate(name):
        if word[0].isalpha() and not word[0].isupper():
            word = word[0].upper() + word[1:]
            name[ind] = word
    print(' '.join(name))


def character_frequency(string):
    """
    Counts the number of characters in a string
    """
    list_freqs = [(char, string.count(char)) for char in string]
    list_freqs.sort(key=lambda x: -x[1])
    freqs_dict = {pair[0]: pair[1] for pair in list_freqs}
    print(freqs_dict)


def beginning_end(string):
    """
    Prints the first 2 and the last 2 characters of a given string
    """
    if len(string) >= 2:
        output = string[:2] + string[-2:]
    else:
        output = ''
    print(output)


def special_strings(array):
    """
    Counts the number of strings with a length of 2 or more and coinciding first and last characters
    """
    fitting_strings = [string for string in array if len(string) >= 2 and string[0] == string[-1]]
    print(len(fitting_strings))


def find_subset(set_1, set_2, set_3):
    """
    Finds out whether set_3 is a subset of both set_1 and set_2
    """
    return all(elem in set_1 and elem in set_2 for elem in set_3)


def dict_generator(number):
    """
    Generates a dictionary with a given number of elements
    """
    dct = {x: x*x for x in range(1, number + 1)}
    print(dct)


def merge_dictionaries(dict_1, dict_2):
    """
    Merges two given dictionaries
    """
    new_dict = {}
    for item in dict_1:
        if item in dict_2:
            new_dict[item] = (dict_1[item], dict_2[item])
            del dict_2[item]
        else:
            new_dict[item] = dict_1[item]
    new_dict.update(dict_2)
    return new_dict


def three_highest(dct):
    """
    Find three highest values in a given dictionary
    """
    highest = list(sorted(dct.values()))[:3]
    print(highest)


def remove_duplicates(array):
    """
    Removes duplicates from a given list
    """
    return set(array)


def lists_difference(array_1, array_2):
    """
    Finds the difference between two given lists
    """
    difference = set(array_1).symmetric_difference(set(array_2))
    return difference
