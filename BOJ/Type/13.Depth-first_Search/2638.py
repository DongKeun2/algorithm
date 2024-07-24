# 치즈
# 34172KB, 820ms

from collections import deque

# BFS로 초기화, 공기를 2로 표현
# 모든 부분이 공기라면 종료
def reset():
    st = deque([(0, 0)])
    vst = [[0]*M for _ in range(N)]
    vst[0][0] = 1
    
    air = 1
    while st:
        si, sj = st.popleft()
        for d in range(4):
            ei, ej = si+di[d], sj+dj[d]
            if 0 <= ei < N and 0 <= ej < M:
                if vst[ei][ej] == 0 and (arr[ei][ej] == 0 or arr[ei][ej] == 2):
                    vst[ei][ej] = 1
                    arr[ei][ej] = 2
                    air += 1
                    st.append((ei, ej))
    if air == N*M:
        return False
    return True


def sol():
    count = 0

    while True:
        # 초기화 후, 치즈마다 공기와 맞닿아 있는 면 cnt 계산
        # cnt가 2 이상이면 해당 치즈자리를 0으로 변경
        # (2로 변경하면 다음 치즈 계산 시 공기로 인식하기 때문) 
        if reset():
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 1:
                        cnt = 0
                        for d in range(4):
                            ei, ej = i + di[d], j + dj[d]
                            if 0 <= ei < N and 0 <= ej < M and arr[ei][ej] == 2:
                                cnt += 1
                        if cnt >= 2:
                            arr[i][j] = 0
            count += 1
        else:
            return count


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

arr[0][0] = 2
print(sol())