# 내리막 길
# 42752KB, 148ms

def sol(si, sj):
    # 도착 시
    if si == end[0] and sj == end[1]:
        return 1

    # 이미 방문한 곳이면 그곳에서 오는 경우의 수 더해주기
    if vst[si][sj] != -1:
        return vst[si][sj]

    # 해당 지점에 올 수 있는 경우의 수 구하기
    cnt = 0
    for d in range(4):
        ei = si + di[d]
        ej = sj + dj[d]
        if 0 <= ei < M and 0 <= ej < N and (arr[si][sj] > arr[ei][ej]):
            cnt += sol(ei, ej)

    # 도착지에서 오르막으로 해당 위치에 올 수 있는 경우의 수
    vst[si][sj] = cnt
    return vst[si][sj]


M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

start = [0,0]
end = [M-1, N-1]
cnt = 0

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

vst = [[-1]*N for _ in range(M)]
result = sol(0, 0)

print(result)
