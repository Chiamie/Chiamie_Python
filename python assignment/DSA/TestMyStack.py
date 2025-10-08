import unittest

from DSA.Array import Array
from DSA.MyStack import MyStack


class TestMyStack(unittest.TestCase):
    def setUp(self):
        self.my_stack = MyStack(5, int)

    def test_that_my_stack_is_empty(self):
        self.assertTrue(self.my_stack.is_empty(), True)

    def test_that_my_stack_contains_an_element(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.my_stack.push(4)
        self.my_stack.push(5)
        self.assertFalse(self.my_stack.is_empty(), False)

    def test_that_my_stack_raises_validation_when_stack_is_full(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.my_stack.push(4)
        self.my_stack.push(5)
        self.assertRaises(IndexError, self.my_stack.push, 6)

    def test_that_the_last_element_is_returned_with_pop_method(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.my_stack.push(4)
        self.my_stack.push(5)
        self.assertEqual(self.my_stack.pop(), 5)

    def test_that_element_is_being_removed_from_the_last_element_of_the_stack(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.my_stack.push(4)
        self.my_stack.push(5)
        self.my_stack.pop()
        self.assertEqual(self.my_stack.get_my_stack(), [1, 2, 3, 4, 0])


if __name__ == '__main__':
    unittest.main()
