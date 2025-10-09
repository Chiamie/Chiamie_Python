from DSA.Array import Array


class ArrayList:
    array_list = []
    count = 0
    size = 0
    def __init__(self, capacity=10, collections=None):
        self.size = capacity
        if collections is not None:
           self.array_list = Array(len(collections), object)
           self.array_list.data[:] = collections
           self.count = len(collections)
        else:
            self.array_list = Array(capacity, object)
            self.count = 0

    def is_empty(self):
        return self.count == 0





