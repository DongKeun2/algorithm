# 지형 이동 Lv4
# Summer/Winter Coding(2019)

# bfs + 다익스트라 풀이
import sys
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def solution(land, height):
    global answer
    # 가장 낮은 설치 비용부터 꺼내어 확인
    # 설치할 수 있는 곳이면 해당 위치에서 sol 실행
    def check(h):
        global answer
        while h:
            c, i, j = heappop(h)
            if vst[i][j] == 0:
                answer += c
                sol(i, j)
                return

    # bfs 돌면서 사다리 필요없는 위치 체크
    # 사다리를 대고 가야하는 곳 heapq에 사다리 높이와 함께 추가
    def sol(i, j):
        vst[i][j] = 1
        q = deque([(i, j)])
        while q:
            si, sj = q.popleft()
            for d in range(4):
                ei = si + di[d]
                ej = sj + dj[d]
                if 0 <= ei < n and 0 <= ej < n and vst[ei][ej] == 0:
                    if abs(land[si][sj] - land[ei][ej]) <= height:
                        vst[ei][ej] = 1
                        q.append((ei, ej))
                    else:
                        heappush(h, (abs(land[si][sj] - land[ei][ej]), ei, ej))
        check(h)
                        
    n = len(land)
    vst = [[0]*n for _ in range(n)]
    h = []
    heappush(h, (0, 0, 0))
    answer = 0
    check(h)
    return answer