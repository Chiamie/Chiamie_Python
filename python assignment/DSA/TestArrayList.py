import unittest

from DSA.ArrayList import ArrayList


class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.array_list = ArrayList(10)

    def test_that_arrayList_is_empty(self):
        self.assertTrue(self.array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_collections(self):
        ages = [34, 23, 12, 45, 2, 37]
        self.my_array_list = ArrayList(collections=ages)
        self.assertFalse(self.my_array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_empty_constructor_and_will_have_10_capacity(self):
        self.my_array_list = ArrayList()
        self.assertEqual(self.my_array_list.size, 10)
        self.assertTrue(self.my_array_list.is_empty())

    def test_that_arrayList_can_be_constructed_using_empty_constructor_and_will_be_empty(self):
        self.my_array_list = ArrayList()
        self.assertTrue(self.my_array_list.is_empty())



if __name__ == '__main__':
    unittest.main()
