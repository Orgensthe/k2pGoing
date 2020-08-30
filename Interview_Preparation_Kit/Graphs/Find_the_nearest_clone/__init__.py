#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
class Graph(object):
    def __init__(self):
        self.graph = {}
        self.val = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, [v])
        self.graph.setdefault(v, [u])

    def set_val(self, u, val):
        self.val[u] = val

    def bfs(self, s):
        distance = 0
        val = self.val[s]
        visited = [0] * (len(self.graph) + 1)

        queue = deque([s])
        visited[s] = 1
        while queue:
            s = queue.pop()
            distance += 1
            for t in self.graph[s]:
                if not visited[t]:
                    if self.val[t] == val:
                        return distance
                    queue.append(t)
                    visited[t] = 1
        return 10 ** 6


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = Graph()
    for u, v in zip(graph_from, graph_to):
        graph.add_edge(u, v)

    for u in range(1, len(ids) + 1):
        graph.set_val(u, ids[u - 1])

    min_distance = 10 ** 6
    for u in range(1, graph_nodes + 1):
        if graph.val[u] == val:
            min_distance = min(min_distance, graph.bfs(u))
    if min_distance == 10 ** 6:
        return -1
    return min_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
