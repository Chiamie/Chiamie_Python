class Array:
    my_array = []
    data_type = None
    count = 0
    size = 0
    def __init__(self, capacity, data_type):
        self.my_array = [data_type()]
        self.size = capacity
        self.data_type = data_type
        self.my_array = self.my_array * self.size


    def is_empty(self):
        return self.count == 0

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.my_array):
            raise IndexError("Array index out of bounds")
        self.validate_data_type(value)
        self.my_array[index] = value

    def __getitem__(self, index):
        if index < 0 or index >= len(self.my_array):
            raise IndexError("Array index out of bounds")
        return self.my_array[index]

    def add(self, value):
        self.validate_data_type(value)
        self.my_array[self.count] = value
        self.count += 1

    def validate_data_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError("Cannot add array with type %s" % self.data_type)

    def remove(self, index):
        self.my_array[index] = self.data_type()

    def get_array(self):
        return self.my_array


