import unittest
import hash_functions

class TestHashFunctions(unittest.TestCase):
    def test_hash_ascii(self):
        a = hash_functions.h_ascii('ABC', 100)
        b = hash_functions.h_ascii('ACB', 100)
        c = hash_functions.h_ascii('ABC', 'test')
        self.assertEqual(a, 98)
        self.assertEqual(a, b)
        self.assertIsNone(c)

    def test_hash_rolling(self):
        a = hash_functions.h_rolling('ABC', 100)
        b = hash_functions.h_rolling('ACB', 100)  
        c = hash_functions.h_rolling('ABC', 'test')
        self.assertNotEqual(a,b)
        self.assertIsNone(c)

if __name__ == '__main__':
    unittest.main()