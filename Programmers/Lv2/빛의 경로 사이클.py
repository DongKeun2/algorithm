# 월간 코드 챌린지 시즌3 Lv2

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solution(grid):
    def sol(si, sj, d):
        cnt = 1
        while True:
            vst[si][sj][d] = cnt
            ni = si + di[d]
            nj = sj + dj[d]
            if ni < 0:
                ni = n - 1
            elif ni >= n:
                ni = 0
                
            if nj < 0:
                nj = m - 1
            elif nj >= m:
                nj = 0

            if grid[ni][nj] == 'L':
                d = (d-1)%4
            elif grid[ni][nj] == 'R':
                d = (d+1)%4

            if vst[ni][nj][d]:
                return cnt
            
            si, sj = ni, nj
            cnt += 1
            
        
    n = len(grid)
    m = len(grid[0])
    vst = [[[0]*4 for _ in range(m)] for _ in range(n)]
           
    answer = []
    while True:
        if sum(answer) >= 4*n*m:
            break
        for i in range(n):
            for j in range(m):
                for k in range(4):
                    if vst[i][j][k] == 0:
                        answer.append(sol(i,j,k))
    answer.sort()
    return answer