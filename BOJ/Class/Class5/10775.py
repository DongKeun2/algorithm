# 공항 / 골드2
# dfs 풀이

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n):
    global flag
    if not flag:
        return
    if n == 0:
        flag = False
        return n
    if n in dct and dct[n] == n:
        dct[n] = n-1
        return n-1
    dct[n] = sol(dct[n])
    return dct[n]

G = int(input())
P = int(input())

dct = {}
for i in range(1, G+1):
    dct[i] = i

flag = True
answer = P
for i in range(P):
    g = int(input())
    sol(g)
    if not flag:
        answer = i
        break
print(answer)