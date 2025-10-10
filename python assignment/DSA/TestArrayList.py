import unittest

from DSA.ArrayList import ArrayList


class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.array_list = ArrayList(int,10)

    def test_that_arrayList_is_empty(self):
        self.assertTrue(self.array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_collections(self):
        ages = [34, 23, 12, 45, 2, 37]
        self.my_array_list = ArrayList(int, values=ages)
        self.assertFalse(self.my_array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_empty_constructor_and_will_have_10_capacity(self):
        my_array_list = ArrayList(int)
        self.assertEqual(my_array_list.size, 10)
        self.assertTrue(my_array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_empty_constructor_and_will_be_empty(self):
        my_array_list = ArrayList(int)
        self.assertTrue(my_array_list.is_empty())

    def test_that_the_capacity_of_arrayList_increases_when_array_is_full(self):
        my_array_list = ArrayList(int,3)
        my_array_list.add(23)
        my_array_list.add(62)
        my_array_list.add(28)
        my_array_list.add(41)

        print(my_array_list)
        print(my_array_list.get_array_list())

        self.assertEqual(my_array_list.get_array_list(),  [23, 62, 28, 41, 0, 0])

    def test_that_arrayList_contains_the_specified_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)

        self.assertTrue(self.array_list.contains(12))

    def test_that_arrayList_does_not_contain_the_specified_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)

        self.assertFalse(self.array_list.contains(42))

    def test_that_arrayList_returns_the_index_of_the_first_occurrence_of_the_specified_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)

        self.assertEqual(self.array_list.index_of(32), 1)


    def test_that_arrayList_returns_the_index_of_the_last_occurrence_of_the_specified_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.last_index_of(12), 4)


    def test_that_arrayList_returns_minus_one_if_the_specified_element_is_not_in_the_arraylist(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.last_index_of(8), -1)

    def test_that_arraylist_
if __name__ == '__main__':
    unittest.main()
