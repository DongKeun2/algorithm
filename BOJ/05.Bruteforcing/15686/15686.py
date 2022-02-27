# 치킨 배달
# 구현 브루트포스
# ing

def f(a):
    pass

def sol(m):
    if m == M:
        f()
        return
    else:
        for i, j in arr2:
            if arr[i][j] == 2:
                arr[i][j] = 0
                sol(m-1)
                arr[i][j]= 2

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr2 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            arr2.append([i, j])

m = len(arr2)

sol(m)