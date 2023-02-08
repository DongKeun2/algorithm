# DFS/BFS Lv3

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    # bfs로 종료지점까지 거리 계산
    def sol(y, x):
        global answer
        q = deque([])
        q.append((y, x))
        vst[y][x] = 0
        while q:
            si, sj = q.popleft()
            if si == itemY*2 and sj == itemX*2:
                answer = vst[si][sj]//2
                return
            for d in range(4):
                ei = si + di[d]
                ej = sj + dj[d]
                if arr[ei][ej] == 1 and vst[ei][ej] == -1:
                    vst[ei][ej] = vst[si][sj] + 1
                    q.append((ei, ej))

    # 테두리만 1로 저장, 올바른 bfs 동작을 위해 2배 확대
    arr = [[0]*102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2, y2*2+1):
            for x in range(x1*2, x2*2+1):
                if x == x1*2 or x == x2*2 or y == y1*2 or y == y2*2:
                    if arr[y][x] != 2:
                        arr[y][x] = 1
                else:
                    arr[y][x] = 2

    answer = 10**18
    vst = [[-1]*102 for _ in range(102)]
    sol(characterY*2, characterX*2)
            
    return answer