# @author: patrickcanny
# BFS implementation and graph class
from collections import deque

class Graph:
    def __init__(self, n):
        self.adjList = [set() for _ in range(n)]
        self.edges = []


    def connect(self, m,n):
        self.adjList[m].add(n)
        self.adjList[n].add(m)
        e = (m,n)
        self.edges.append(e)

def find_all_distances(self, s):
    #BFS Traversal
    Q = deque()
    seen = [0 for _ in range(len(self.adjList))]
    dist = [-1 for _ in range(len(self.adjList))]

    seen[s] = 1
    dist[s] = 0
    Q.append(s)

    while len(Q) != 0:
        v = Q.popleft()
        height = dist[v]
        children = self.adjList[v]
        for u in children:
            if seen[u] != 1:
                seen[u] = 1
                Q.append(u)
                dist[u] = height + 6

    for i in range(len(dist)):
        if dist[i] != 0:
            print(dist[i], end=' ', flush = True)
    print()


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
