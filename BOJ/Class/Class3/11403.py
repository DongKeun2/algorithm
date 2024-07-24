# 경로 찾기, 실버1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not arr[i][j] and arr[i][k] and arr[k][j]: arr[i][j] = 1

for answer in arr:
    print(*answer)