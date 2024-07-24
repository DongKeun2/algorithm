# 안전 영역
# 34120KB, 724ms

from collections import deque

def sol(n):
    global result

    tmp = [[-1]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            # 잠기지 않는 지대에서 cnt + 1
            # BFS, 연결된 곳 표시
            if tmp[i][j] == -1 and arr[i][j] > n:
                tmp[i][j] = 0
                count += 1
                st = deque([(i, j)])
                while st:
                    si, sj = st.popleft()
                    for d in range(4):
                        ei = si + di[d]
                        ej = sj + dj[d]
                        if 0 <= ei < N and 0 <= ej < N and tmp[ei][ej] == -1 and arr[ei][ej] > n:
                            tmp[ei][ej] = 0
                            st.append((ei, ej))
    if result < count:
        result = count


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 브루트 포스, 비가 안오는 경우부터 모두 잠길 경우까지 안전한 지대계산
result = 0
for n in range(101):
    sol(n)

print(result)