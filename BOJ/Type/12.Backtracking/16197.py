# 두 동전
# 그래프 이론, 그래프 탐색, 백트래킹, 너비우선탐색

# 두 동전의 좌표, 이동 횟수
def sol(ci1, cj1, ci2, cj2, cnt):
    global result

    # 이미 구한 결과값보다 많이 이동한 경우
    if result < cnt:
        return

    # 10번 넘게 이동한 경우
    if cnt > 10:
        return
    
    # 두 동전이 동시에 떨어진 경우
    if (ci1 <= 0 or ci1 > N or cj1 <= 0 or cj1 > M) and (ci2 <= 0 or ci2 > N or cj2 <= 0 or cj2 > M):
        return

    # 1번 동전만 떨어진 경우
    if (ci1 <= 0 or ci1 > N or cj1 <= 0 or cj1 > M) and 0 < ci2 <= N and 0 < cj2 <= M:
        if result > cnt:
            result = cnt
        return

    # 2번 동전만 떨어진 경우
    if (ci2 <= 0 or ci2 > N or cj2 <= 0 or cj2 > M) and 0 < ci1 <= N and 0 < cj1 <= M:
        if result > cnt:
            result = cnt
        return

    # 한 동전이라도 이동하려는 곳이 벽이 아니라면 이동
    for d in range(4):
        ni1, nj1 = ci1 + di[d], cj1 + dj[d]
        ni2, nj2 = ci2 + di[d], cj2 + dj[d]
        if arr[ni1][nj1] != '#' and arr[ni2][nj2] != '#':
            sol(ni1, nj1, ni2, nj2, cnt+1)
        elif arr[ni1][nj1] != '#':
            sol(ni1, nj1, ci2, cj2, cnt+1)
        elif arr[ni2][nj2] != '#':
            sol(ci1, cj1, ni2, nj2, cnt+1)


N, M = map(int, input().split())

# 낙하하는 동전을 확인하기 위해 겉에 빈 칸을 만들어 줌
arr = [['.']*(M+2)] + [['.'] +list(input()) + ['.'] for _ in range(N)] + [['.']*(M+2)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 두 동전의 위치 저장
coin = []
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j] == 'o':
            coin.append([i, j])
ci1, cj1 = coin[0][0], coin[0][1]
ci2, cj2 = coin[1][0], coin[1][1]

# 최댓값 저장
result = N*M
sol(ci1, cj1, ci2, cj2, 0)

# 결과가 갱신되지 않았으면 불가능한 경우
if result == N*M:
    result = -1

print(result)
