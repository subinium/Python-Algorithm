# [BOJ 11404] 플로이드
# link : https://www.acmicpc.net/problem/11657
# tag : graph, floyd-warshall, shortest path
# @subinium

# Floyd-Warshall Algorthm
# time complexity : O(V^3)
def floyd_warshall(v, edge):
    INF = 1e10
    dist = [[INF for _ in range(v+1)] for _ in range(v+1)]     
    for st, ed, val in edge : 
        dist[st][ed] = min(dist[st][ed], val)

    # mid(중간), st(출발), ed(도착) 순서 중요
    for mid in range(1, v):
        for st in range(1, v+1):
            for ed in range(1, v+1):
                dist[st][ed] = min(dist[st][ed], dist[st][mid]+dist[mid][ed])

    # 자기자신으로 가는 루트
    for i in range(v+1): dist[i][i] = INF 
    return dist

# Main
if __name__ == '__main__':
    n, m = int(input()), int(input())
    edge = [tuple(map(int, input().split())) for _ in range(m)] # (from, to, time) 
    dist = floyd_warshall(n, edge)
    
    for row in dist[1:]:
        print(' '.join([str(int(i * (i!=1e10))) for i in row[1:]]))