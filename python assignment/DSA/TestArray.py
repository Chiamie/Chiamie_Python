import unittest

from DSA.Array import Array


class TestArray(unittest.TestCase):
    def setUp(self):
        self.array = Array(5, int)

    def test_that_array_is_empty(self):
        self.assertTrue(self.array.is_empty(), True)

    def test_that_array_is_not_empty(self):
        self.array.add(1)
        self.assertFalse(self.array.is_empty(), False)

    def test_that_array_has_fixed_size(self):
        self.array.add(1)
        self.array.add(2)
        self.array.add(3)
        self.array.add(4)
        self.array.add(5)
        self.assertEqual(self.array.get_array(), [1, 2, 3, 4, 5])

    def test_that_array_has_default_element_at_instantiation(self):
        self.assertEqual(self.array.get_array(), [0, 0, 0, 0, 0])

    def test_that_the_default_element_replaces_the_index_of_an_element_when_removed(self):
        self.array.add(1)
        self.array.add(2)
        self.array.add(3)
        self.array.add(4)
        self.array.add(5)
        self.array.remove(3)
        self.assertEqual(self.array.get_array(), [1, 2, 3, 0, 5])

    def test_that_(self):
        self.array[0] = 12
        self.array[1] = 12
        self.array[2] = 12
        self.array[3] = 12
        self.array[4] = 12
        self.array[5] = 12


if __name__ == '__main__':
    unittest.main()
