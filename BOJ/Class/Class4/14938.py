# 서강그라운드 / 골드4

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
arr = [[10**16]*N for _ in range(N)]
for _ in range(R):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = c
    arr[b-1][a-1] = c

for m in range(N):
    arr[m][m] = 0
    for s in range(N):
        if not m == s:
            for e in range(N):
                if not s == e and arr[s][e] > arr[s][m] + arr[m][e]:
                    arr[s][e] = arr[s][m] + arr[m][e]

answer = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] <= M:
            cnt += items[j]
    if answer < cnt:
        answer = cnt
print(answer)

