# [BOJ 2150] Strongly Connected Component 
# link : https://www.acmicpc.net/problem/2150
# tag : graph, SCC, Kosaraju, DFS, stack
# @subinium

import sys
sys.setrecursionlimit(10000) # 재귀함수 런타임에러 방지

# Kosaraju 
def kosaraju(v, edge_raw):
    stack, scc = [], [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    edge, edge_rev = [[] for _ in range(v+1)], [[] for _ in range(v+1)]
    for st, ed in edge_raw:
        edge[st].append(ed)
        edge_rev[ed].append(st)

    # DFS for stack & reverse
    def dfs(now, group=0):
        visited[now] = True
        if group: scc[group].append(now)
        for nxt in (edge[now] if group else edge_rev[now]):
            if not visited[nxt]: dfs(nxt, group)
        if not group: stack.append(now)

    for i in range(1, v+1):
        if not visited[i]: dfs(i)

    num_groups = 0
    visited = [False for _ in range(v+1)]

    for i in stack[::-1]:
        if not visited[i]:
            num_groups += 1
            dfs(i, num_groups)

    return num_groups, scc[1: 1+num_groups]


# Main
if __name__ == '__main__':
    input = sys.stdin.readline
    V, E = map(int, input().split())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    num_groups, scc = kosaraju(V, edge)
    for i in range(num_groups):
        scc[i].sort()
        scc[i].append(-1)

    print(num_groups)
    for group in sorted(scc):
        print(' '.join(map(str, group)))
