# [BOJ 11657] 타임머신
# link : https://www.acmicpc.net/problem/11657
# tag : graph, bellman-ford, shortest path, negative cycle
# @subinium

# Bellman-Ford Algorthm
def bellman_ford(v, edge, start=1):
    INF = 1e10
    dist = [INF for _ in range(v+1)]
    dist[start] = 0
    for i in range(1, v+1):
        for st, ed, val in edge: # start, end, value
            if dist[st] == INF: continue
            if dist[ed] > dist[st] + val: 
                dist[ed] = dist[st] + val
                if i == v : return None, True
    return dist, False

# Main
if __name__ == '__main__':
    N, M = map(int, input().split())
    edge = [tuple(map(int, input().split())) for _ in range(M)] # (from, to, time) 
    dist, neg = bellman_ford(N, edge)
    if neg : print(-1) # Negative Cycle
    else : print('\n'.join(map(str, [i if i!=1e10 else -1 for i in dist[2:]])))
