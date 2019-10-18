import hash_functions
import argparse
import sys
import time 
import os
import random

def reservoir_sampling(new_val, size, V):
    """
    This function generates a list of keys to be searched

    Parameters
    ----------
    new_val : str
        new value to be searched

    size : int
        number of keys to be searched

    V : list 
        list of values to be searched

    Returns
    -------
    None
    """
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val

class LinearProbe:
    def __init__(self, N, hash_fucntion):
        """
        The initilization function takes in the size of the hash table and the
        hash function

        Parameters
        ----------
        N : int
            the size of the hash table
        hash_function : function
            the hash function for generating a hash table

        Returns
        -------
        None
        """
        self.hash_fucntion = hash_fucntion
        self.N = N                          
        self.T = [None for i in range(N)]  # Hash table 
        self.M = 0   # number of pair inserted

    def add(self, key, value):
        """
        This functions insert a key-value pair to a slot of the hash table using
        the linear probing approach

        Parameters
        ----------
        key : str
            the key of the corresponding value
        value : float
            the value to be stored in the slot in the hash table

        Returns
        -------
        insert : bool
            Whether the pair is inserted or not
        """
        start_hash = self.hash_fucntion(key, self.N)
        insert = False
        
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                insert = True
                return insert
        return insert

    def search(self, key):
        """
        This function returns the value corresponding to a given key using a
        linear probing approach.

        Parameters
        ----------
        key : str
            the key for the searching 

        Returns
        -------
        val : float or NoneType
            the value of the given key or None if no corresponding value was 
            found
        """
        start_hash = self.hash_fucntion(key, self.N)
        val = None
        
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                val = None
                return val
            if self.T[test_slot][0] == key:
                val = self.T[test_slot][1]
                return val
        return val


class ChainedHash:
    def __init__(self, N, hash_fucntion):
        """
        The initilization function takes in the size of the hash table and the
        hash function

        Parameters
        ----------
        N : int
            the size of the hash table
        hash_function : function
            the hash function for generating a hash table

        Returns
        -------
        None
        """
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [ [] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """
        This functions insert a key-value pair to a slot of the hash table using
        the chained hash approach

        Parameters
        ----------
        key : str
            the key of the corresponding value
        value : float
            the value to be stored in the slot in the hash table

        Returns
        -------
        True
        """
        start_hash = self.hash_fucntion(key, self.N)
        self.T[start_hash].append((key,value))
        self.M += 1
        return True

    def search(self, key):
        """
        This function returns the value corresponding to a given key using a
        chained hash approach.

        Parameters
        ----------
        key : str
            the key for the searching 

        Returns
        -------
        val : float or NoneType
            the value of the given key or None if no corresponding value was 
            found
        """
        start_hash = self.hash_fucntion(key, self.N)
        val = None 
        for k, v in self.T[start_hash]:
            if key == k:
                val = v
                return val
        return val

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='This Python code performs several experiments on different \
                    hash algorithms and collision resolution strategy in a hash \
                    table.',
        prog='HashTables')

    parser.add_argument('-n',
                        '--size',
                        type=int,
                        help='The size of the hash table')

    parser.add_argument('-a',
                        '--algorithm',
                        type=str,
                        help='The hash algorithm to be used. Available options are \
                             "ascii" and "rolling"')
    parser.add_argument('-s',
                        '--collision',
                        type=str,
                        help='The collision resolution strategy. Available options \
                             are "LP" (linear probling) and "CH" (chained hash)')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='The file name of the input file.')
    parser.add_argument('-k',        
                        '--n_key',
                        type=int,
                        help='Number of keys to add')
    
    args = parser.parse_args()

    ht = None
    if args.algorithm == 'ascii':

        if args.collision == 'LP':
            ht = LinearProbe(args.size, hash_functions.h_ascii)
        elif args.collision == 'CH':
            ht = ChainedHash(args.size, hash_functions.h_ascii)
        else:
            print('Please input the collision resolution strategies available, \
                either "LP" or "CH".')
            sys.exit(1)

    elif args.algorithm == 'rolling':

        if args.collision == 'LP':
            ht = LinearProbe(args.size, hash_functions.h_rolling)
        elif args.collision == 'CH':
            ht = ChainedHash(args.size, hash_functions.h_rolling)
        else:
            print('Please input the collision resolution strategies available, \
                either "LP" or "CH".')
            sys.exit(1)
    else:
        print('Please input the hash algorithms available, either "ascii" or "rolling".')
        sys.exit(1)
    
    keys_to_search = 100   # number of keys to search
    V = []

    if (not os.path.exists(args.input)):
        print('Input file not found')
        sys.exit(1)

    for l in open(args.input):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l,l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == args.n_key:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1-t0)