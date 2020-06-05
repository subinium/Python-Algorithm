# [BOJ 1753] 최단경로
# link : https://www.acmicpc.net/problem/1753
# tag : graph, dijkstra, shortest path
# @subinium

import sys
from heapq import heappop, heappush

# Dijkstra Algorithm 
def dijkstra(v, start, edge_raw):
    INF = 1e10
    edge = [[] for _ in range(v+1)]
    # Adjacency list
    for st, ed, val in edge_raw: edge[st].append((val, ed))
    dist = [INF for _ in range(v+1)]
    dist[start] = 0
    hq = [(0, start)]
    while len(hq):
        val, st = heappop(hq)
        if dist[st] < val : continue
        for val_edge, ed in edge[st]:
            if dist[ed] > dist[st] + val_edge:
                dist[ed] = dist[st] + val_edge
                heappush(hq, (dist[ed], ed))
    return dist

# Main
if __name__ == '__main__':
    input = sys.stdin.readline # fastio
    V, E = map(int, input().split())
    K = int(input())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    dist = dijkstra(V, K, edge)
    print('\n'.join([str(i) if i!=1e10 else 'INF' for i in dist[1:]]))