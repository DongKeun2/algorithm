# 구간 합 구하기 4

N, M = map(int, input().split())

lst = list(map(int, input().split()))

tmp = [0] * (N+1)
for i in range(1, N+1):
    tmp[i] = tmp[i-1] + lst[i-1]

for i in range(M):
    s, e = map(int, input().split())
    result = tmp[e] - tmp[s-1]
    print(result)
