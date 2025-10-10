import collections

from DSA.Array import Array


class ArrayList:
    count = 0
    size = 0

    def __init__(self, data_type, capacity=10, values=None):
        self.array_list = [data_type()]
        self.data_type = data_type
        self.size = capacity
        if values is not None:
           self.array_list = Array(len(values), data_type)
           self.array_list.data[:] = values
           print(self.array_list)
           self.count = len(values)
        else:
            self.array_list = Array(capacity, data_type)
            self.count = 0

    def is_empty(self):
        return self.count == 0

    def __resize(self, new_capacity):
        new_array = Array(new_capacity, self.data_type)
        for index in range(self.count):
            new_array.data[index] = self.array_list.data[index]
        self.array_list = new_array
        self.array_list.size = new_capacity

    def add(self, value):
        if self.count == self.size:
            self.__resize(self.size * 2)
        self.array_list[self.count] = value
        self.count += 1

    def get_array_list(self):
        return self.array_list

    def contains(self, value):
        for index in range(0, self.size):
            if self.array_list[index] == value:
                return True
        return False

    def index_of(self, value):
        for index in range(0, self.size):
            if self.array_list[index] == value:
                return index
        return -1

    def last_index_of(self, value):
        index = -1
        for counter in range(0, self.size):
            if self.array_list[counter] == value:
                index = counter
        return index

    def
    get(int
    index){
    if (index < 0 | | index >= array.length)
    throw
    new
    IndexOutOfBoundsException("Index is out of bounds!");
    return array[index];
    }

    public
    Object
    set(int
    index, Object
    value){
    if (index < 0 | | index >= array.length)
        throw
        new
        IndexOutOfBoundsException("Index is out of bounds!");

    Object
    oldValue = array[index];
    array[index] = value;
    return oldValue;

}

def __str__(self):
        return str(self.array_list)

    def __repr__(self):
        print(self.array_list)







