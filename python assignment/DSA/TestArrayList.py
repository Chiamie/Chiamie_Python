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

    def test_that_arraylist_returns_the_element_at_the_specified_position_in_this_list(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.get(3), 41)

    def test_that_arrayList_raises_exception_when_the_specified_position_in_the_list_is_not_found(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertRaises(IndexError, self.array_list.get, 9)


    def test_that_the_element_at_the_specified_position_in_this_list_is_replaced_with_the_specified_element_and_the_previous_element_is_returned(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.set(3, 102), 41)

    def test_that_the_element_at_the_specified_position_in_this_list_is_replaced_with_the_specified_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)
        self.array_list.set(3, 102)

        self.assertEqual(self.array_list.get_array_list(), [12, 32, 21, 102, 12, 53, 0, 0, 0, 0])

    def test_that_arrayList_raises_exception_when_the_specified_position_in_the_list_is_not_found_while_using_the_set_method(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertRaises(IndexError, self.array_list.set, 9, 112)

    def test_that_arrayList_returns_an_array_containing_all_of_the_elements_in_this_arraylist_in_proper_sequence_from_first_to_last_element(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.to_array(), [12, 32, 21, 41, 12, 53])


    def test_that_the_element_at_the_specified_position_in_this_list_is_removed_and_is_confirm_by_returning_the_removed_value(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)

        self.assertEqual(self.array_list.remove(2), 21)

    def test_that_the_element_at_the_specified_position_in_this_list_is_removed_then_shifts_any_subsequent_elements_to_the_left(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)
        self.array_list.remove(2)

        self.assertEqual(self.array_list.get_array_list(), [12, 32, 41, 12, 53, 0, 0, 0, 0, 0])

    def test_that_removes_from_this_list_all_of_its_elements_that_are_contained_in_the_specified_collection(self):
        self.array_list.add(12)
        self.array_list.add(32)
        self.array_list.add(21)
        self.array_list.add(41)
        self.array_list.add(12)
        self.array_list.add(53)
        self.array_list.remove_all([41, 16, 32])

        self.assertEqual(self.array_list.get_array_list(), [12, 32, 21, 12, 53, 0, 0, 0, 0, 0])










if __name__ == '__main__':
    unittest.main()
