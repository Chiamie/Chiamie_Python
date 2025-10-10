class Array:

    def __init__(self, capacity, data_type):
        self.data = [data_type()]
        self.size = capacity
        self.data_type = data_type
        self.data = self.data * self.size
        self.count = 0


    def is_empty(self):
        return self.count == 0

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("Array index out of bounds")
        self.validate_data_type(value)
        self.data[index] = value

    def __getitem__(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Array index out of bounds")
        return self.data[index]

    def add(self, value):
        self.validate_data_type(value)
        self.data[self.count] = value
        self.count += 1

    def __validate_data_type(self, value):
        if not isinstance(value, self.data_type):
            raise TypeError("Cannot add array with type %s" % self.data_type)


    def remove(self, index):
        self.data[index] = self.data_type()

    def get_array(self):
        return self.data

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, Array):
            return self.data == other.data
        elif isinstance(other, list):
            return self.data == other
        else:
            return False


