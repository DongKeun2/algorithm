# 성적 평균 Lv3

import sys
input = sys.stdin.readline

# 누적합 활용 풀이
N, K = map(int, input().split())
lst = list(map(int, input().split()))
tmp = [0] * (N+1)
tmp[1] = lst[0]
for i in range(1, N):
    tmp[i+1] = tmp[i] + lst[i]

for _ in range(K):
    s, e = map(int, input().split())
    print(round((tmp[e] - tmp[s-1]) / (e-s+ 1), 2))