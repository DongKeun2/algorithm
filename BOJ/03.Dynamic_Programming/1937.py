# 욕심쟁이 판다
# 51372KB, 1068ms

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs, 시작점으로부터 가장 큰 곳까지 이동
# 큰 곳을 1로 하여 저장 이어진 곳 +1씩
def sol(si, sj):
    global result
    if tmp[si][sj] != 0:
        return tmp[si][sj]
    else:
        tmp[si][sj] = 1

    # 네 방향 중 가장 긴 곳에 연결하여 저장, 없다면 1로 종료
    for d in range(4):
        ei, ej = si + di[d], sj + dj[d]
        if 0 <= ei < N and 0 <= ej < N and arr[ei][ej] > arr[si][sj]:
                tmp[si][sj] = max(tmp[si][sj], sol(ei, ej) + 1)
    
    # 저장된 값 확인하여 갱신
    if result < tmp[si][sj]:
        result = tmp[si][sj]

    return tmp[si][sj]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

tmp = [[0]*N for _ in range(N)]
di = [1, 0 ,-1, 0]
dj = [0, 1, 0, -1]

result = 0
for i in range(N):
    for j in range(N):
        sol(i, j)

print(result)