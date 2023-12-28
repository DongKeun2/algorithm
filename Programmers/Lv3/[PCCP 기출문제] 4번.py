# [PCCP 기출문제] 4번 / 수레 움직이기

# dfs 풀이
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solution(maze):
    global answer
    def dfs(rsi, rsj, bsi, bsj, cnt):
        global answer
        if maze[rsi][rsj] == 3 and maze[bsi][bsj] == 4:
             if answer > cnt:
                    answer = cnt
                    return
        # 빨강 도착한 경우
        if maze[rsi][rsj] == 3:
            for d in range(4):
                bei, bej = bsi + di[d], bsj + dj[d]
                if 0 <= bei < n and 0 <= bej < m and maze[bei][bej] != 5 and vst[1][bei][bej] == 0 and not (bei == rsi and bej == rsj):
                    vst[1][bei][bej] = 1
                    dfs(rsi, rsj, bei, bej, cnt+1)
                    vst[1][bei][bej] = 0
            return
        # 파랑 도착한 경우
        if maze[bsi][bsj] == 4:
            for d in range(4):
                rei, rej = rsi + di[d], rsj + dj[d]
                if 0 <= rei < n and 0 <= rej < m and maze[rei][rej] != 5 and vst[0][rei][rej] == 0 and not (rei == bsi and rej == bsj):
                    vst[0][rei][rej] = 1
                    dfs(rei, rej, bsi, bsj, cnt+1)
                    vst[0][rei][rej] = 0
            return
        for dr in range(4):
            rei, rej = rsi + di[dr], rsj + dj[dr]
            if 0 <= rei < n and 0 <= rej < m and maze[rei][rej] != 5 and vst[0][rei][rej] == 0:
                for db in range(4):
                    bei, bej = bsi + di[db], bsj + dj[db]
                    if 0 <= bei < n and 0 <= bej < m and maze[bei][bej] != 5 and vst[1][bei][bej] == 0 and not (bei == rei and bej == rej) and not (rei == bsi and rej == bsj and bei == rsi and bej == rsj):
                        vst[0][rei][rej], vst[1][bei][bej] = 1, 1
                        dfs(rei, rej, bei, bej, cnt+1)
                        vst[0][rei][rej], vst[1][bei][bej] = 0, 0
    
    
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rsi = i
                rsj = j
            if maze[i][j] == 2:
                bsi = i
                bsj = j
    answer = 10**16
    vst = [[[0] * m for _ in range(n)], [[0] * m for _ in range(n)]]
    vst[0][rsi][rsj], vst[1][bsi][bsj] = 1, 1
    dfs(rsi, rsj, bsi, bsj, 0)
    
    return 0 if answer == 10**16 else answer