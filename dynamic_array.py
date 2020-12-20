import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def append(self, value):
        if self.n == self.capacity:
            self._resize()
        self.A[self.n] = value
        self.n += 1

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def _resize(self):
        temp = self.make_array(self.capacity * 2)
        for k in range(self.n):
            temp[k] = self.A[k]

        self.A = temp
        self.capacity *= 2
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError(f'{K} is out of bounds')
        return self.A[k]
    