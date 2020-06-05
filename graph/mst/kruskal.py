# [BOJ 1197] 최소 스패닝 트리
# link : https://www.acmicpc.net/problem/1197
# tag : graph, mininum spanning tree, MST, kruskal, union find
# @subinium

import sys

# Kruskal Algorithm
def kruskal(v, edge):
    edge = sorted(edge, key=lambda x: x[2])
    parent = [i for i in range(v+1)]
    result = 0

    def find_(num):
        if num == parent[num] : return num
        parent[num] = find_(parent[num])
        return parent[num]

    def union_(a, b):
        if a < b : parent[a] = b
        else : parent[b] = a

    for st, ed, val in edge:
        v, w = find_(st), find_(ed)
        if v == w : continue
        union_(v, w)
        result += val
    
    return result

if __name__ == '__main__':
    input = sys.stdin.readline 
    V, E = map(int, input().split())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    result = kruskal(V, edge)
    print(result)