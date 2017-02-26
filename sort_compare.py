#!/usr/bin/env python
# -*- coding utf-8 -*-
"""Week 4 Assignment 4 Part 2"""

import time
import random

def insertion_sort(l): # l = list
    """
    Args:
        l(list): List of numbers.

    Returns:
        l(list): Sorted List.

    Examples:
        >>> insertion_sort([1,2,3,4,5,6,7,8,9,10])
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.0067901611328125e-06)
    """
    s = time.time() # s = start
    for index in range(1, len(l)):

        current_value = l[index]
        position = index

        while position > 0 and l[position - 1] > current_value:
            l[position] = l[position - 1]
            position = position - 1
            l[position] = current_value
        end = time.time()
        return l, end-s

def shell_sort(l): # l = list
    """
    Args:
        l(list): List of numbers.

    Returns:
        l(list): List of number sorted.

    Examples:
        >>> shell_sort([9,8,7,6,5,4,3,2])
        ([2, 3, 4, 5, 6, 7, 8, 9], 2.5987625122070312e-05)
    """
    s = time.time() # s = start
    sublist_count = len(l) // 2

    while sublist_count > 0:
        for s_position in range(sublist_count):
            is_gap(l, s_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return l, end-s

def is_gap(l, s, gap): # s = start, l =  list
    """
    Args:
        l(list): List of numbers.

    Returns:

    Examples:

    """
    for i in range(s + gap, len(l), gap):
        current_value = l[i]
        position = i
        while position >= gap and l[position - gap] > current_value:
            l[position] = l[position - gap]
            position = position - gap
        l[position] = current_value

def python_sort(l): # l = list
    """The python_sort function simply a ‘wrapper’ function that calls
        sort() on the input list.
    Args:
        l(list): List of numbers.

    Returns:
        l(list): Sorted list.

    Examples:
        >>> python_sort([3,2,1])
            ([1, 2, 3, 6, 8], 3.0994415283203125e-06)
    """
    s = time.time() # s = start, l =  list
    l.sort()
    end = time.time()
    return l, end-s

def ran_number(value):
    """
    Args:
        random_list(list): List of random ints based on values.

    Returns:
        random_list(list): Creates list of random values fast.

    Examples:
        >>> ran_number(100)
        [79, 1, 76, 62, 31, 21, 23, 27, 85, 0, 24, 25, 53, 32, 87, 46,
        11, 12, 41, 29, 81, 71, 69, 36, 90, 15, 57, 82, 96, 48, 37, 59, 63,
        80, 30, 54, 13, 94, 9, 77, 92, 72, 42, 51, 61, 91, 67, 43, 84, 93,
        49, 8, 88, 89, 97, 2, 5, 28, 40, 10, 47, 55, 44, 60, 83, 34, 73,
        99, 98, 52, 4, 16, 18, 95, 35, 75, 65, 6, 50, 86, 26, 17, 38, 66,
        78, 14, 74, 3, 70, 39, 64, 22, 33, 45, 20, 58, 19, 7, 68, 56]
    """
    random_list = random.sample(range(0, value), value)
    return random_list


def main():
    """
    Args:
        test dict): Test keys and values.
        random_list(list): Generated  random lists
        inter_count(int): Interger of indexed count.
        ouput(dict): Results output

    Returns:
        None

    Examples:
        >>> main()
        List of 500 length the test timed:
        Insertion Sort took  0.0000065 seconds to run on average
        Shell Sort took  0.0010760 seconds to run on average
        Python Sort took  0.0000131 seconds to run on average

        List of 1000 length the test timed:
        Insertion Sort took  0.0000092 seconds to run on average
        Shell Sort took  0.0016598 seconds to run on average
        Python Sort took  0.0000194 seconds to run on average

        List of 10000 length the test timed:
        Insertion Sort took  0.0000706 seconds to run on average
        Shell Sort took  0.0283402 seconds to run on average
        Python Sort took  0.0001699 seconds to run on average
    """
    tests = {'test1': 500,
             'test2': 10000,
             'test3': 1000}
    for test in tests.values():
        random_list = ran_number(test)
        iter_count = 100
        output = {'insert':0,
                  'shell':0,
                  'pyth':0}
        while iter_count > 0:
            output['insert'] += insertion_sort(random_list)[1]
            output['shell'] += shell_sort(random_list)[1]
            output['pyth'] += python_sort(random_list)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test
        print "Insertion Sort took %10.7f seconds to run on average" % \
              (float(output['insert'] / 100))
        print "Shell Sort took %10.7f seconds to run on average" % \
              (float(output['shell'] / 100))
        print "Python Sort took %10.7f seconds to run on average" % \
              (float(output['pyth'] / 100))
        print '\n'

if __name__ == '__main__':
    main()
