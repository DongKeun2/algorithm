# 비밀번호 찾기, 실버4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dct = {}
for _ in range(N):
    key, value = map(str, input().strip().split())
    dct[key] = value

lst = []
for _ in range(M):
    target = input().strip()
    lst.append(dct[target])
for answer in lst:
    print(answer)