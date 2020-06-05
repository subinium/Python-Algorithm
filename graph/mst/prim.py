# [BOJ 1197] 최소 스패닝 트리
# link : https://www.acmicpc.net/problem/1197
# tag : graph, mininum spanning tree, MST, prim, priority queue
# @subinium

import sys
from heapq import heappush, heappop

# Prim
def prim(v, edge_raw):
    checked = [False for _ in range(v+1)] 
    edge = [[] for _ in range(v+1)]
    for st, ed, val in edge_raw: 
        edge[st].append((val, ed))
        edge[ed].append((val, st))

    pq = [(0, 1)]
    result = 0
    while pq:
        val, node = heappop(pq)
        if checked[node]: continue 
        checked[node] = True
        result += val
        for val, ed in edge[node]:
            if checked[ed] : continue
            heappush(pq, (val, ed))

    return result

# Main
if __name__ == '__main__':
    input = sys.stdin.readline 
    V, E = map(int, input().split())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    result = prim(V, edge)
    print(result)