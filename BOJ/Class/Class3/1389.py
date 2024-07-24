# 케빈 베이컨의 6단계 법칙, 실버1
# 플로이드 와셜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[10**9]*N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not k == i and not k == j: arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = (0, 10**9)
for i in range(N):
    s = sum(arr[i])
    if s < answer[1]: answer = (i, s)

print(answer[0]+1)