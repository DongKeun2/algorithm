# 홈 방범 서비스

# bfs
def sol(si, sj, k):
    global result

    q = []
    q.append([si, sj])
    vst = [[0 for _ in range(N)] for _ in range(N)]
    vst[si][sj] = 1
    
    # 방범 서비스 받은 home 수
    cnt = 0
    
    # 시작지점이 집이면 1 추가하고 시작
    if arr[si][sj] == 1:
        cnt += 1
    while q:
        si, sj = q.pop(0)
        n = vst[si][sj]
        # k만큼 이동한 모양 완. 성.
        if vst[si][sj] >= k:
            if cost[k] <= cnt*M and result < cnt:
                result = cnt
            return
        # 4방향으로 탐색
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]
            # 갈 수 있는 곳이면 go
            if 0 <= ni < N and 0 <= nj < N and vst[ni][nj] == 0 and arr[ni][nj] == 0:
                vst[ni][nj] = n + 1
                q.append([ni, nj])
            # 갈 수 있는 집이면 cnt 증가
            elif 0 <= ni < N and 0 <= nj < N and vst[ni][nj] == 0 and arr[ni][nj] == 1:
                vst[ni][nj] = n + 1
                q.append([ni, nj])
                cnt += 1


T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

# k에 따른 방범 비용 저장
cost = [n**2 for n in range(22)]
for i in range(1, 22)[::-1]:
    cost[i] += cost[i-1]

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 도시의 총 집 수 tot
    tot = 0
    for i in range(N):
        tot += arr[i].count(1)
        
    # 도시 전체 방범 시 모든 집 방범 서비스 가능
    if cost[N+1] <= tot*M:
        result = tot
    
    # 도시 전체 방범할 비용 없으면 탐색
    else:
        result = 0
        flag = 0
        for i in range(N):
            if flag == 1:
                break
            for j in range(N):
                if flag == 1:
                    break
                for k in range(1, N+2):
                    if result >= tot:
                        flag = 1
                        break
                    elif cost[k] > result:
                        sol(i, j, k)

    print(f'#{test_case} {result}')
