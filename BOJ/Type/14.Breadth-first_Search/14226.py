# 이모티콘

from collections import deque

# bfs
def sol():
    q = deque()
    q.append([1, 0])
    arr[1][0] = 0
    while q:
        n, c = q.popleft()

        if n == S:
            break

        # 복사하기
        if arr[n][n] == 100001:
            arr[n][n] = arr[n][c] + 1
            q.append([n, n])

        # 붙여넣기
        if n+c <= S and arr[n+c][c] == 100001:
            arr[n+c][c] = arr[n][c] + 1
            q.append([n+c, c])

        # 하나 지우기
        if n-1 >= 0 and arr[n-1][c] == 100001:
            arr[n-1][c] = arr[n][c] + 1
            q.append([n-1, c])
    

S = int(input())

arr = [[100001]*(S+1) for _ in range(S+1)]

sol()

print(min(arr[S]))