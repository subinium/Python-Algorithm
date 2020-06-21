# [BOJ 2609] 최대공약수와 최소공배수
# link : https://www.acmicpc.net/problem/2609
# tag : math, 유클리드 호제법
# @subinium

def gcd(a, b):
    return gcd(b, a % b) if a % b else b


def lcm(a, b):
    return a * b // gcd(a, b)


# Main
if __name__ == '__main__':
    A, B = map(int, input().split())
    print(gcd(A, B))
    print(lcm(A, B))
