# [BOJ 11438] LCA 2
# link : https://www.acmicpc.net/problem/11438
# tag : graph, tree, LCA, Sparse Tree
# @subinium

import sys 
from collections import deque

# Make Tree with BFS
def make_tree(v, edge_raw, root):
    edge = [[] for _ in range(v+1)]
    for a, b in edge_raw: 
        edge[a].append(b)
        edge[b].append(a)

    check, depth, tree = [[0 for _ in range(v+1)] for _ in range(3)]
    check[root] = True

    q = deque([root])
    while len(q):
        now = q.popleft()
        for nxt in edge[now]:
            if check[nxt] : continue
            depth[nxt] = depth[now] + 1
            check[nxt] = True
            tree[nxt] = now
            q.append(nxt)

    return tree, depth

# Make Sparse Tree 
def sparse_tree(v, tree):
    p = [[0 for _ in range(18)] for _ in range(v+1)]
    for i in range(1, v+1): p[i][0] = tree[i]
    bit = 1
    while 2**bit < v :
        for i in range(1, v+1):
            if p[i][bit-1] != 0:
                p[i][bit] = p[p[i][bit-1]][bit-1]
        bit+=1
    return p

# Optimized LCA
def lca(tree, depth, sparse, u, v):
    if depth[u] < depth[v] : u, v = v, u
    bit = 1
    while 2**(bit-1) <= depth[u] : bit+=1
    
    for i in range(bit, -1, -1) : 
        if depth[u] - 2**i >= depth[v]: u = sparse[u][i]

    if u == v : return u
    for i in range(bit, -1, -1):
        if sparse[u][i] != 0 and sparse[u][i] != sparse[v][i]: 
            u, v = sparse[u][i], sparse[v][i]
    return tree[u]

# Main
if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    edge = [tuple(map(int, input().split())) for _ in range(N-1)]
    tree, depth = make_tree(N, edge, 1)
    sparse = sparse_tree(N, tree)

    M = int(input())
    for _ in range(M):
        u, v = map(int, input().split())
        print(lca(tree, depth, sparse, u, v))