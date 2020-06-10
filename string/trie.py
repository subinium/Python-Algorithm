# [BOJ 5052] 전화번호 목록
# link : https://www.acmicpc.net/problem/5052
# tag : string, trie, insert, search
# @subinium

import sys

# Trie Class
# 기존 Trie는 insert와 search 과정이 필요
# 하지만 여기서는 insert로 확인가능
class Trie(object):
    def __init__(self):
        self.nxt = [None for _ in range(10)]
        self.goexist = False
        self.output = False

    def insert(self, string, idx):
        if len(string) == idx: 
            self.output = True
            return self.goexist 
 
        char = ord(string[idx])-ord('0')
        if self.nxt[char] == None : self.nxt[char] = Trie()
        self.goexist = True
        return self.output or self.nxt[char].insert(string, idx+1)
    
# Test Case 별 Process
def process():
    N = int(input())
    root = Trie()
    result = True
    for _ in range(N):
        string = input().replace('\n','')
        if result and root.insert(list(string), 0): result = False
    print ('YES' if result else 'NO')

# Main : Test Case 존재
if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T): process()