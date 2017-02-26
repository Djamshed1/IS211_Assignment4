#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Assignment 4 Part 1"""

import time
import random

def sequential_search(l, i): #l = list, i =  item
    """
    Args:
        l(list): List of numbers.
        i(int): It finds numbers in the list.

    Returns:
        found(bool): Return true if item is available.

    Examples:
        >>> sequential_search([2,3,6,1], 1)
        (True, 3.0994415283203125e-06)
    """
    s = time.time()
    pos = 0
    found = False

    while pos < len(l) and not found:
        if l[pos] == i:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end-s

def ordered_sequential_search(l, i): #l = list, i =  item
    """
    Args:
        l(list): List of numbers.
        i(int): It finds numbers in the list.
        
    Returns:
        found(bool): Return true if item is available.
        
    Examples:
        >>> ordered_sequential_search([2,3,4,9,8,7], 1)
        (False, 1.6927719116210938e-05)
    """
    s = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(l) and not found and not stop:
        if l[pos] == i:
            found = True
        else:
            if l[pos] > i:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    return found, end-s

def binary_search_iterative(l, i): #l = list, i =  item
    """
    Args:
        l(list): List of numbers.
        i(int): It finds numbers in the list.

    Returns:
        found(bool): Return true if item is available.

    Examples:
        >>> binary_search_iterative([9,8,7,6,1,2,3], 1)
        (True, 5.0067901611328125e-06)
    """
    s = time.time()
    l.sort()
    first = 0
    last = len(l) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if l[midpoint] == i:
            found = True
        else:
            if i < l[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-s

def binary_search_recursive(l, i): #l = list, i =  item
    """
    Args:
        l(list): List of numbers.
        i(int): It finds numbers in the list.
        
    Returns:
        found(bool): Return true if item is available.

    Examples:
        >>> binary_search_recursive([1,3,5,7,9,1,3], 1)
        (True, 1.3828277587890625e-05) 
    """
    s = time.time()
    l.sort()

    if len(l) == 0:
        found = False
    else:
        midpoint = len(l) // 2

        if l[midpoint] == i:
            found = True
        else:
            if i < l[midpoint]:
                return binary_search_iterative(l[:midpoint], i)
            else:
                return binary_search_iterative(l[midpoint + 1:], i)

    end = time.time()
    return found, end-s

def ran_number(value):
    """
    Args:

    Returns:
        random_list(list): Returns random numbers.

    Examples:
        >>> ran_number(100)
        [65, 27, 77, 25, 66, 6, 44, 92, 56, 32, 82, 58, 13, 3, 72, 79, 87,
        78, 28, 35, 46, 20, 67, 84, 96, 14, 95, 39, 30, 88, 50, 22, 91, 21,
        26, 90, 93, 41, 57, 12, 36, 9, 33, 89, 68, 51, 17, 4, 37, 74, 1,
        38, 2, 45, 42, 60, 15, 99, 94, 10, 63, 24, 31, 97, 73, 18, 75,
        61, 8, 80, 81, 29, 76, 40, 55, 47, 69, 62, 5, 34, 83, 54, 16, 64,
        7, 48, 85, 71, 19, 11, 0, 52, 43, 86, 23, 49, 53, 70, 59, 98]
    """
    random_list = random.sample(range(0, value), value)
    return random_list

def main():
    """
    Args:

    Returns:

    Examples:
        >>> main()
        List of 500 length the test timed:
        Sequential took  0.0001603 seconds to run on average
        Ordered Seq took  0.0000010 seconds to run on average
        Binary Iter took  0.0000275 seconds to run on average
        Binary Recur took  0.0000118 seconds to run on average

        List of 1000 length the test timed:
        Sequential took  0.0001678 seconds to run on average
        Ordered Seq took  0.0000007 seconds to run on average
        Binary Iter took  0.0000278 seconds to run on average
        Binary Recur took  0.0000091 seconds to run on average

        List of 10000 length the test timed:
        Sequential took  0.0015195 seconds to run on average
        Ordered Seq took  0.0000083 seconds to run on average
        Binary Iter took  0.0002074 seconds to run on average
        Binary Recur took  0.0001005 seconds to run on average
    """
    tests = {'test1': 500,
             'test2': 10000,
             'test3': 1000}

    for test in tests.values():
        random_list = ran_number(test)
        iter_count = 100
        output = {'seq':0,
                  'ord_seq':0,
                  'bin_iter':0,
                  'bin_recur':0}
        while iter_count > 0:
            output['seq'] += sequential_search(random_list, -1)[1]
            output['ord_seq'] += ordered_sequential_search(random_list, -1)[1]
            output['bin_iter'] += binary_search_iterative(random_list, -1)[1]
            output['bin_recur'] += binary_search_recursive(random_list, -1)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test

        print "Sequential took %10.7f seconds to run on average" % \
              (float(output['seq']/ 100))
        print "Ordered Seq took %10.7f seconds to run on average" % \
              (float(output['ord_seq'] / 100))
        print "Binary Iter took %10.7f seconds to run on average" % \
              (float(output['bin_iter']/ 100))
        print "Binary Recur took %10.7f seconds to run on average" % \
        (float(output['bin_recur']/ 100))
        print '\n'


if __name__ == '__main__':
    main()
