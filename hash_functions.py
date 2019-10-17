import sys
import argparse

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

if __name__ == '__main__':

    for l in open()

