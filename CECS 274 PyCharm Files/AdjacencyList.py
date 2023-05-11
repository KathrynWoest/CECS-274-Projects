"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def size(self):
        return self.n

    def add_edge(self, i : int, j : int):
        if i >= self.n or j >= self.n:
            raise IndexError
        if j not in self.adj[i]:
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if i >= self.n or j >= self.n:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if i >= self.n or j >= self.n:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        if i >= self.n:
            raise IndexError
        return self.adj[i]

    def in_edges(self, i) -> list:
        if i >= self.n:
            raise IndexError
        incoming = []
        for k in range(self.n):
            if self.has_edge(k, i):
                incoming.append(k)
        return incoming

    def bfs(self, r : int):
        seen = []
        for i in range(self.n):
            seen.append(False)
        q = ArrayQueue.ArrayQueue()
        traversal = []
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while len(q) != 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for j in neighbors:
                if seen[j] == False:
                    q.add(j)
                    traversal.append(j)
                    seen[j] = True
        return traversal

    def dfs(self, r : int):
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = []
        for i in range(self.n):
            seen.append(False)
        s.push(r)
        while len(s) != 0:
            current = s.pop()
            if seen[current] == False:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            for i in reversed(neighbors):
                if seen[i] == False:
                    s.push(i)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
