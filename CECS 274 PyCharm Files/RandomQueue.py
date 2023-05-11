import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n <= 0:
            raise IndexError
        rand_int = random.randint(self.j, self.n - 1)
        rand_element = self.a[rand_int]
        head_element = self.a[self.j]
        self.a[self.j] = rand_element
        self.a[rand_int] = head_element
        removed = super().remove()
        return removed
