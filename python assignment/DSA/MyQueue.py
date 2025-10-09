from DSA.Array import Array


class MyQueue:
    my_queue = None
    data_type = None
    count = 0

    def __init__(self, capacity, data_type):
        self.data_type = data_type
        self.my_queue = Array(capacity, data_type)


    def is_empty(self):
        return self.count == 0

    def add(self, value):
        if value is not None:
            if isinstance(value, self.data_type):
                if self.count != self.my_queue.size:
                    self.my_queue[self.count] = value
                    self.count += 1
                    return True
                else:
                    raise Exception("Queue is full")
            else:
                raise Exception("IllegalArgument Exception: Unacceptable value")
        else:
            raise Exception(" Null Pointer Exception: Null element is not allowed")

    def get_queue(self):
        return self.my_queue

    def offer(self, value):
        if value is not None:
            if isinstance(value, self.data_type):
                if self.count != self.my_queue.size:
                    self.my_queue[self.count] = value
                    self.count += 1
                    return True
                else:
                    return False
            else:
                raise Exception("IllegalArgument Exception: Unacceptable value")
        else:
            raise Exception(" Null Pointer Exception: Null element is not allowed")

    def remove(self):
        if not self.is_empty():
            head = self.my_queue[0]
            self.my_queue.remove(0)
            return head
        else:
            raise Exception("No Such Element Exception: Queue is empty")









