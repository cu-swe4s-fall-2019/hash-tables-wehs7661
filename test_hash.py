import unittest
import hash_functions
import hash_tables


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
        self.assertNotEqual(a, b)
        self.assertIsNone(c)


class TestHashTables(unittest.TestCase):
    def test_linear_probing(self):
        ht1 = hash_tables.LinearProbe(1000, hash_functions.h_ascii)
        ht2 = hash_tables.LinearProbe(1000, hash_functions.h_rolling)
        ht1.add('ABC', 30)
        ht2.add('ABC', 30)
        self.assertEqual(ht1.search('ABC'), 30)
        self.assertEqual(ht1.search('DEF'), None)
        self.assertEqual(ht2.search('ABC'), 30)
        self.assertEqual(ht2.search('DEF'), None)

    def test_chained_hash(self):
        ht1 = hash_tables.ChainedHash(1000, hash_functions.h_ascii)
        ht2 = hash_tables.ChainedHash(1000, hash_functions.h_rolling)
        ht1.add('ABC', 30)
        ht2.add('ABC', 30)
        self.assertEqual(ht1.search('ABC'), 30)
        self.assertEqual(ht1.search('DEF'), None)
        self.assertEqual(ht2.search('ABC'), 30)
        self.assertEqual(ht2.search('DEF'), None)


if __name__ == '__main__':
    unittest.main()
