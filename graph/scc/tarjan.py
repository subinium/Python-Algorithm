# [BOJ 2150] Strongly Connected Component 
# link : https://www.acmicpc.net/problem/2150
# tag : graph, SCC, Tarjan, DFS, stack
# @subinium

import sys
sys.setrecursionlimit(10000) # 재귀함수 런타임에러 방지

# Tarjan Algorithm 
def tarjan(v, edge_raw):
    stack, scc, cnt = [], [], [0] # cnt를 내부함수 전역변수로 쓰기 위해 
    visited, finished = [0 for _ in range(v+1)], [False for _ in range(v+1)]
    edge = [[] for _ in range(v+1)]
    for st, ed in edge_raw: edge[st].append(ed)

    def dfs(now):
        cnt[0] += 1
        visited[now] = cnt[0]
        stack.append(now)
        result = visited[now]

        for nxt in edge[now]:
            if visited[nxt] == 0: result = min(result, dfs(nxt))
            elif not finished[nxt]: result = min(result, visited[nxt])

        if result == visited[now]:
            group = []
            while True:
                top = stack.pop()
                group.append(top)
                finished[top] = True
                if top == now: break
            scc.append(group)        
        
        return result

    for i in range(1, v+1):
        if visited[i] == 0: dfs(i)

    return len(scc), scc


# Main
if __name__ == '__main__':
    input = sys.stdin.readline
    V, E = map(int, input().split())
    edge = [tuple(map(int, input().split())) for _ in range(E)]
    num_groups, scc = tarjan(V, edge)
    for i in range(num_groups):
        scc[i].sort()
        scc[i].append(-1)

    print(num_groups)
    for group in sorted(scc):
        print(' '.join(map(str, group)))
