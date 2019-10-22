import os
import sys
import argparse
import numpy as np


def h_ascii(key, N):
    """
    This function takes a string key and a hash table szie and returns a hash
    that is based on the sum of the ASCII values for the characters in the key

    Parameters
    ----------
    key : str
        the key of the value to be stored
    N : int
        the size of the hash table

    Returns
    -------
    s_mod : int
        a hash that is based on the sum of the ASCII values for the characters
        in the key
    """
    try:
        N = int(N)
    except ValueError:
        print('The size of the hash table (N) should be an integer.')
        return None
    key = str(key)
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    s_mod = s % N
    return s_mod


def h_rolling(key, N, p=53, m=2**64):
    """
    This function takes a string key and a hash table size to return a hash
    that is based on the polynomial rolling hash algorithm.

    Parameters
    ----------
    key : str
        the key of the value to be stored
    N : int
        the size of the hash table
    p : int
        a prime number roughly equal to the number of characters in the input.
        p is frequently set as 53
    m : int
        m should be a large number, since the probability of two random strings
        colliding is about 1/m. m=2^64 is frequently used.

    Returns
    -------
    s_mod : int
        a hash that is based on the polynomial rolling hash algorithm
    """
    try:
        N = int(N)
    except ValueError:
        print('The size of the hash table (N) should be an integer.')
        return None
    key = str(key)
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p ** i
    s = s % m
    s_mod = s % N
    return s_mod


def h_myown(key, N, m=2069):
    """
    This function takes a string key and a hash table size to return a hash
    that is based on the ASCII code and the position of the character.

    Parameters
    ----------
    key : str
        the key of the value to be stored
    N : int
        the size of the hash table
    p : int
        a prime number, here the default is 2069

    Returns
    -------
    s_mod : int
        a hash corresponding to the key
    """

    try:
        N = int(N)
    except ValueError:
        print('The size of the hash table (N) should be an integer.')
        return None
    key = str(key)
    s = 0
    for i in range(len(key)):
        s += (ord(key[i]) * 10 + i) * i
    s = s % m
    s_mod = s % N
    return s_mod


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='A Python module of different hash methods',
        prog='hash_functions'
    )

    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='The file name of the input file.')
    parser.add_argument('-m',
                        '--method',
                        type=str,
                        help='Hash methods. Available options are: "ascii" \
                        "rolling" and "myown".')
    args = parser.parse_args()

    if (not os.path.exists(args.input)):
        print('Input file not found')
        sys.exit(1)

    for l in open(args.input):
        if (args.method == 'ascii'):
            print(h_ascii(l, 100000))
        elif (args.method == 'rolling'):
            print(h_rolling(l, 100000))
        elif (args.method == 'myown'):
            print(h_myown(l, 100000))
        else:
            print('Please input the hash methods avaiable, including "ascii" \
                  ,"rolling" or "myown".')
            sys.exit(1)
