#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    # Dictionary로 Graph, Color dict 만들기
    graph = defaultdict(list)
    colors = defaultdict(int)

    for i in range(len(graph_from)):

        # Graph 양방향 연결
        graph[graph_from[i]].append(graph_to[i])
        graph[graph_to[i]].append(graph_from[i])

        # color 양방향 연결
        if graph_from[i] not in colors:
            colors[graph_from[i]] = ids[graph_from[i] -1]
        if graph_to[i] not in colors:
            colors[graph_to[i]] = ids[graph_to[i]-1]

    # 방문 예정 큐(BFS를 위함)
    bfs_queue = deque()

    # 시작 노드 정해주기
    bfs_queue.append((val, 0))

    # 시작 노드의 컬러 정해주기
    start_color = colors[val]

    # 방문한 목록
    visited = set()

    while bfs_queue:

        # 현재 노드 가져오기
        current_node, count = bfs_queue.popleft()

        # 방문 목록 확인
        visited.add(current_node)

        # 각 노드별 갈 수 있는 곳 순차 방문
        for path in graph[current_node]:
            # 이미 방문했는지 확인
            if path not in visited:
                # 색 같은지 확인
                if colors[path] == start_color:
                    # 색 같으면 해당 노드까지 오는데 걸린 횟수 리턴
                    return count + 1
                # 방문하지 않았었으면 방문 목록에 추가
                visited.add(path)
                # 방문할 예정으로 추가
                bfs_queue.append((path, count + 1))
    #갈 수 없음
    return -1

if __name__ == '__main__':
    fptr = sys.stdout

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
