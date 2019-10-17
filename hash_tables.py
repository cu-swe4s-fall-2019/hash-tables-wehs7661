import hash_functions
import argparse

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
                    table.'
        prog='HashTables'
    )

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
    parser.add_argument('-o',
                        '--input',
                        type=str,
                        help='The file name of the input file.')
    parser.add_argument('-k',
                        '--key',
                        type=int,
                        help='')
    
    args = parser.parse_args()

