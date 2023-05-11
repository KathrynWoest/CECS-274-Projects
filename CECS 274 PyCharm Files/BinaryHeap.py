import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree
import SLLQueue


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        # if 3 * self.n < len(self.a):
        #     self._resize()
        return x

    def depth(self, u) -> int:
        try:
            in_a = False
            for i in range(len(self.a)):
                if u == self.a[i]:
                    in_a = True
                    u_idx = i
                    break
            if not in_a:
                raise ValueError
            d = 0
            while u_idx != 0:
                u_idx = parent(u_idx)
                d += 1
            return d
        except ValueError:
            print(f"{u} is not found in the binary tree.")

    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> object:
        bf_heap = []
        for i in range(self.n):
            bf_heap.append(self.a[i])
        return bf_heap

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self, i):
        initial = self.a[0]
        u = self.a[i]
        elements = []
        if left(i) <= self.n:
            elements.extend(self._in_order(left(i)))
        if u >= initial:
            elements.append(u)
        if right(i) <= self.n:
            elements.extend(self._in_order(right(i)))
        return elements

    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, i):
        initial = self.a[0]
        u = self.a[i]
        elements = []
        if left(i) <= self.n:
            elements.extend(self._post_order(left(i)))
        if right(i) <= self.n:
            elements.extend(self._post_order(right(i)))
        if u >= initial:
            elements.append(u)
        return elements

    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self, i):
        initial = self.a[0]
        u = self.a[i]
        elements = []
        if u >= initial:
            elements.append(u)
        if left(i) <= self.n:
            elements.extend(self._pre_order(left(i)))
        if right(i) <= self.n:
            elements.extend(self._pre_order(right(i)))
        return elements

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            x = self.a[i]
            y = self.a[p_idx]
            self.a[i] = y
            self.a[p_idx] = x
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        b = _new_array(max(1, 2 * self.n))
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b

    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        while i < self.n and l_idx < self.n and r_idx <= self.n and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            min_element = min(self.a[i], self.a[l_idx], self.a[r_idx])
            if min_element == self.a[i]:
                min_idx = i
            elif min_element == self.a[l_idx]:
                min_idx = l_idx
            else:
                min_idx = r_idx
            x = self.a[i]
            y = self.a[min_idx]
            self.a[i] = y
            self.a[min_idx] = x
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)


    def __str__(self):
        return str(self.a[0:self.n])
