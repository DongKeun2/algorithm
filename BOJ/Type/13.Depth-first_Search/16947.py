# 서울 지하철 2호선
import sys
from collections import deque
input = sys.stdin.readline

# dfs
def sol(s):
    vst = [0] * (N+1)
    vst[s] = 1
    st = deque()
    st.append(s)
    while st:
        n = vst[s]
        for x in arr[s]:
            # 아직 방문하지 않았다면 vst에 기록하며 방문
            if vst[x] == 0:
                vst[x] = n+1
                st.append(s)
                s = x
                break
            
            # 첫 지점으로 돌아올 수 있으면 순환선에 포함
            elif vst[s] != 2 and vst[x] == 1:
                result.append(0)
                return

            # 첫 지점으로 돌아오지 않는다면 그 지점과 첫 지점의 차이 구하기
            elif vst[s]+1 != vst[x] and vst[s]-1 != vst[x]:
                result.append(vst[x]-1)
                return
        else:
            s = st.pop()


N = int(input())

# 인접리스트 생성
arr = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = []
for i in range(1, N+1):
    sol(i)

print(*result)
