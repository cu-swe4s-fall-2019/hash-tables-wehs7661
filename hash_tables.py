import hash_functions

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