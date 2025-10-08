from DSA.Array import Array


class MyStack:
    my_stack = Array(5, int)
    count = 0

    def is_empty(self):
        return self.count == 0


    def push(self, value):
        if self.count != self.my_stack.size:
            self.my_stack[self.count] = value
            self.count += 1
        else:
            raise IndexError("Stack Overflow")


