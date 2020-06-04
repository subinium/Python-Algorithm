# [BOJ 1768] 찾기
# link : https://www.acmicpc.net/problem/1786
# tag : string, kmp, failure
# @subinium

# Failure function
def failure(P):
    pl = len(P)
    fail, j = [0 for _ in range(pl)], 0
    for i in range(1, pl):
        while j > 0 and P[i] != P[j] : j = fail[j-1]
        if P[i]==P[j]: fail[i], j = j+1, j+1
    return fail

# KMP Algorithm
# time complexity : O(len(T) + len(P))
def kmp(T, P):
    fail = failure(P)
    fail, res, j, tl, pl = failure(P), [], 0, len(T), len(P)
    for i in range(tl):
        while j > 0 and T[i] != P[j]: j = fail[j-1]
        if T[i]==P[j]: 
            if j == pl-1:
                res.append(i-pl+2)
                j = fail[j]
            else : j+=1
    return res

# Main
if __name__ == '__main__':
    T, P = input(), input()
    result = kmp(T, P)
    print(len(result))
    for idx in result: print(idx)
