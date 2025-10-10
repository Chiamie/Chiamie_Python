import collections
from itertools import count

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
        for counter in range(0, self.count):
            if self.array_list[counter] == value:
                index = counter
        return index

    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index is out of bounds!")
        return self.array_list[index]

    def set(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index is out of bounds!")
        old_value = self.array_list[index]
        self.array_list[index] = value
        return old_value

    def to_array(self):
        number_of_elements = 0
        for index in range(self.count):
            if self.array_list[index] is not None:
                number_of_elements += 1
        new_array = Array(number_of_elements, self.data_type)
        new_index = 0
        for index in range(self.count):
            if self.array_list[index] is not None:
                new_array[new_index] = self.array_list[index]
                new_index += 1
        return new_array

    def remove(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index is out of bounds!")
        old_value = self.array_list[index]
        for counter in range(index, self.count):
            self.array_list[counter] = self.array_list[counter+1]
        self.array_list[self.count - 1] = self.data_type()
        return old_value

    #def remove(self, value):
        result = False
        for index in range(self.count):
            if self.array_list[index] == value:
                self.array_list[index] = self.data_type()
                result = True
        return result

    def remove_all(self, values):
        print(self.array_list)
        changed = False
        for index in range(len(values)):
            for index2 in range(self.count):
                if self.array_list[index2] == values[index]:
                    print(self.array_list.data_type)
                    if self.array_list.data_type == self.data_type():
                    self.array_list[index2] = self.data_type
                    changed = True
        return changed

    def validate
        elif all(type(item) != int for item in value):
            raise ValueError("list_of_numbers must all be integers")




    def __str__(self):
        return str(self.array_list)

    def __repr__(self):
        print(self.array_list)







