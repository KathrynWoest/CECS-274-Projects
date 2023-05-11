from SLLQueue import SLLQueue
from DLLDeque import DLLDeque

class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface & inherits all methods from DLList

    def add(self, x: object):
        """adds an element to the end of this max queue
        INPUT: x the element to add"""
        super().add(x)
        if self.max_deque.n == 0:
            self.max_deque.add(0, x)
        elif x > self.max_deque.get(0):
            self.max_deque.dummy = DLLDeque.Node("")
            self.max_deque.dummy.next = self.max_deque.dummy
            self.max_deque.dummy.prev = self.max_deque.dummy
            self.max_deque.n = 0
            self.max_deque.add(0, x)
        else:
            check = False
            location = self.max_deque.n
            for i in range(1, self.max_deque.n):
                if not x < self.max_deque.get(i):
                    self.max_deque.set(i, x)
                    location = i
                    check = True
                    break
            if not check:
                self.max_deque.add_last(x)
            for i in range(location + 1, self.max_deque.n):
                self.max_deque.remove_last()

    def remove(self) -> object:
        """removes and returns the element at the head of the max queue"""
        if self.n == 0:
            raise IndexError
        x = super().remove()
        if x == self.max_deque.dummy.next.x:
            self.max_deque.remove_first()
        return x
    def max(self):
        """returns the maximum element stored in the queue"""
        return self.max_deque.get(0)



"""
# TESTER
mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")"""
