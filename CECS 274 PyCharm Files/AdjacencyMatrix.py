from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def size(self):
        return self.n

    def add_edge(self, i : int, j : int):
        if i >= self.n or j >= self.n:
            raise IndexError
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        if i >= self.n or j >= self.n:
            raise IndexError
        if self.adj[i][j] == True:
            self.adj[i][j] = False
            return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if i >= self.n or j >= self.n:
            raise IndexError
        if self.adj[i][j] == 1:
            return True
        else:
            return False

    def out_edges(self, i) -> list:
        edges = []
        for j in range(self.n):
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, j) -> list:
        edges = []
        for x in range(self.n):
            if self.adj[x][j] == 1:
                edges.append(x)
        return edges

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
