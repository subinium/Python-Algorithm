# [BOJ 11758] CCW
# link : https://www.acmicpc.net/problem/11758
# tag : geometry, vector
# @subinium

from operator import sub

# CCW : Counter-Clock-Wise
# vector subtraction : tuple(map(sub, p1, p2)) 
def ccw(a, b, c):
    a, c = tuple(map(sub, a, b)), tuple(map(sub, c, b))
    return a[0]*c[1]-a[1]*c[0]

# Main
if __name__ == '__main__':
    p1, p2, p3 = [tuple(map(int, input().split())) for _ in range(3)]
    ans = ccw(p1, p2, p3)
    print(0 if ans==0 else -int(ans/abs(ans)))