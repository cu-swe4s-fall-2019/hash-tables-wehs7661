
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


def h_rolling(key, N):

    return None


def h_python(key, N):
    pass



