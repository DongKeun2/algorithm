# Two Dots
import sys
input=sys.stdin.readline

# dfs
# 시작지점의 색깔 s로 받아줌
def sol(si, sj, s):
    global result

    # 매 순간 시작지점에 1 저장 후 시작
    vst = [[0 for _ in range(M)] for _ in range(N)]
    vst[si][sj] = 1
    st = []
    st.append([si, sj])
    while st:
        n = vst[si][sj]

        # 상하좌우 탐색
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]
            # 색깔이 같고 아직 방문하지 않았다면 방문
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == s and vst[ni][nj] == 0:
                vst[ni][nj] = n+1
                st.append([si, sj])
                si, sj = ni, nj
                break
            # 시작지점으로 돌아왔다면 사이클이 성립하는 지 확인
            elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == s and vst[ni][nj] == 1 and n != 2:
                if n >= 4:
                    result = 'Yes'
                    return
        else:
            si, sj = st.pop()


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 결과값에 No 입력, 사이클이라면 Yes로 바꿔주고 종료
result = 'No'
for i in range(N):
    if result == 'Yes':
        break
    for j in range(M):
        if result == 'Yes':
            break
        sol(i, j, arr[i][j])

print(result)
