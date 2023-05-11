from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy
        if i < self.n / 2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy.prev
            for k in range(self.n - i - 1):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i > self.n:
            raise IndexError
        u = self.get_node(i)
        return u.x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError
        node = self.get_node(i)
        old = node.x
        node.x = x
        return old

    def add_before(self, w: Node, x: object) -> Node:
        if w is None:
            raise IndexError
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        palindrome = DLList()
        for i in range(self.n):
            y = str(self.get(i))
            if y.isalnum():
                palindrome.add(i, y.lower())
        y = palindrome.dummy.next
        z = palindrome.dummy.prev
        for i in range(palindrome.n // 2):
            if y.x != z.x:
                return False
            y = y.next
            z = z.prev
        return True

    def reverse(self):
        reversed_list = DLList()
        y = self.dummy.prev
        for i in range(self.n):
            reversed_list.add(i, y.x)
            y = y.prev
        for i in range(reversed_list.n):
            self.remove(0)
        x = reversed_list.dummy.next
        for i in range(reversed_list.n):
            self.add(i, x.x)
            x = x.next

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
