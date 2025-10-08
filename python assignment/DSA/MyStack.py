from DSA.Array import Array


class MyStack:
    my_stack = None
    data_type = None
    count = 0
    def __init__(self, capacity, data_type):
        self.data_type = data_type
        self.my_stack = Array(capacity, data_type)


    def is_empty(self):
        return self.count == 0


    def push(self, value):
        if self.count != self.my_stack.size:
            self.my_stack[self.count] = value
            self.count += 1
        else:
            raise IndexError("Stack Overflow")

    def pop(self):
        if self.count > 0:
            self.count -= 1
            element_to_remove = self.my_stack[self.count]
            self.my_stack[self.count] = self.data_type()
            return element_to_remove
        else:
            raise IndexError("Stack Underflow")

    def size(self):
        return self.count

    def peek(self):
        if self.count != 0:
            self.count -= 1
            return self.my_stack[self.count]
        raise Exception("Empty Stack Exception")

    def search(self, value):
        if self.count != 0:
            for index in range(0, self.size()):
                if index == self.size() - 1:
                    return 1
                elif self.my_stack[index] == value:
                    return index
                else:
                    return -1
        raise Exception("Empty Stack Exception")



def get_my_stack(self):
        return self.my_stack


