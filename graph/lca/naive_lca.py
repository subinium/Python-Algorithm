# [BOJ 11437] LCA
# link : https://www.acmicpc.net/problem/11437
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

# Naive LCA
def lca(tree, depth, u, v):
    if depth[u] < depth[v] : u, v = v, u
    while depth[u] != depth[v]: u = tree[u]
    while u != v : u, v = tree[u], tree[v]
    return u

# Main
if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    edge = [tuple(map(int, input().split())) for _ in range(N-1)]
    tree, depth = make_tree(N, edge, 1)
    
    M = int(input())
    for _ in range(M):
        u, v = map(int, input().split())
        print(lca(tree, depth, u, v))