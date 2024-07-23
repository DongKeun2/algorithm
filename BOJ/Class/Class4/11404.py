# 플로이드 / 골드4

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[10**16] * N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)


for m in range(N):
    for s in range(N):
        if not s == m:
            for e in range(N):
                if not s == e and arr[s][e] > arr[s][m] + arr[m][e]:
                    arr[s][e] = arr[s][m] + arr[m][e]
        
for lst in arr:
    print(' '.join([str(x) if not x == 10**16 else '0' for x in lst]))