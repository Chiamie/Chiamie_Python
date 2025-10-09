import unittest

from DSA.MyQueue import MyQueue


class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.my_queue = MyQueue(5, str)

    def test_that_my_queue_is_empty(self):
        self.assertTrue( self.my_queue.is_empty(), True)  # add assertion here

    def test_that_my_queue_is_not_empty(self):
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Priest")
        self.my_queue.add("Makaveli")
        self.assertFalse(self.my_queue.is_empty(), False)

    def test_that_an_exception_is_raise_when_my_queue_is_full_and_element_is_being_added(self):
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Priest")
        self.my_queue.add("Makaveli")
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Basit")
        self.assertRaises(Exception, self.my_queue.add, "Queue is full" )

    def test_that_an_exception_is_raise_when_element_of_different_type_is_to_be_added_to_a_queue_of_specified_type(self):
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Priest")
        self.my_queue.add("Makaveli")
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Basit")
        self.assertRaises(Exception, self.my_queue.add, 56)

    def test_that_an_exception_is_raise_when_a_default_value_is_to_be_added_to_my_queue(self):
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Priest")
        self.my_queue.add("Makaveli")
        self.my_queue.add("Chiamaka")
        self.my_queue.add("Basit")
        self.assertRaises(Exception, self.my_queue.add, None)


    def test_that_an_exception_is_raise_when_my_queue_is_full_and_element_is_being_inserted_using_offer_method(self):
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Priest")
        self.my_queue.offer("Makaveli")
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Basit")
        self.assertRaises(Exception, self.my_queue.offer, False)

    def test_that_an_exception_is_raise_when_element_of_different_type_is_to_be_added_to_a_queue_of_specified_type_using_the_offer_method(self):
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Priest")
        self.my_queue.offer("Makaveli")
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Basit")
        self.assertRaises(Exception, self.my_queue.offer, 56)

    def test_that_an_exception_is_raise_when_a_default_value_is_to_be_added_to_my_queue_while_using_the_offer_method(self):
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Priest")
        self.my_queue.offer("Makaveli")
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Basit")
        self.assertRaises(Exception, self.my_queue.offer, None)

    def test_that_the_first_element_on_the_list_is_removed_from_the_queue(self):
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Priest")
        self.my_queue.offer("Makaveli")
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Basit")
        self.my_queue.remove()
        expected = ["", "Priest", "Makaveli", "Chiamaka", "Basit"]
        self.assertEqual(expected, self.my_queue.get_queue())

    def test_that_the_first_element_on_the_list_is_returned_from_the_queue_while_using_remove_method(self):
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Priest")
        self.my_queue.offer("Makaveli")
        self.my_queue.offer("Chiamaka")
        self.my_queue.offer("Basit")
        expected = "Chiamaka"
        self.assertEqual(expected, self.my_queue.remove())

if __name__ == '__main__':
    unittest.main()
