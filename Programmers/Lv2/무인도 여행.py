# 연습문제 Lv2

# 방향
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def solution(maps):
    # bfs로 무인도 연결
    def bfs(i, j):
        vst[i][j] = 1
        q = [(i, j)]
        cnt = int(maps[i][j])
        while q:
            si, sj = q.pop(0)
            for d in range(4):
                ei = si + di[d]
                ej = sj + dj[d]
                if 0 <= ei < n and 0 <= ej < m:
                    if maps[ei][ej] != 'X' and not vst[ei][ej]:
                        cnt += int(maps[ei][ej])
                        vst[ei][ej] = 1
                        q.append((ei, ej))
        return cnt
    
    
    n, m = len(maps), len(maps[0])
    
    # 무인도 식량 answer에 저장
    answer = []
    vst = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not vst[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
    
    # 무인도가 있으면 오름차순 정렬, 없다면 -1 담아 반환
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer