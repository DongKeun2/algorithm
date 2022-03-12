# 유기농 배추
# 깊이 우선 탐색, 너비 우선 탐색, 그래프 이론, 그래프 탐색

# 테스트 케이스 수
T = int(input())

# 상, 하, 좌, 우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
for _ in range(T):

    # arr에 배추밭 정보 입력
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    # cnt : 배추흰지렁이 투입 수
    cnt = 0
    for i in range(N):
        for j in range(M):

            # 배추가 있으면 배추흰지렁이 투입
            if arr[i][j] == 1:
                cnt += 1
                st = [[i, j]]
                
                # 접근 가능한 모든 배추 보호
                while st:
                    ii, jj = st.pop()
                    for d in range(4):
                        ni = ii + di[d]
                        nj = jj + dj[d]
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                            arr[ni][nj] = 0
                            st.append([ni, nj])
    print(cnt)
    