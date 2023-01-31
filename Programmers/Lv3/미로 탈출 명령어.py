# 2023 카카오 블라인드
# Lv3

import sys
sys.setrecursionlimit(10**6)

di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]
S = ['d', 'l', 'r', 'u']

def sol(si, sj, cnt, word, n, m, r, c, k):
    global answer
    
    if answer != 'impossible':
        return
    
    # k만큼 이동했을 때 도착지인지 확인
    if cnt >= k:
        if si == r and sj == c:
            answer = word
        return
    
    # 백트래킹 : 남은 이동 횟수로 도착이 불가능한 경우
    if k - cnt < abs(r-si) + abs(c-sj):
        return

    # dlru(사전순)으로 DFS
    for d in range(4):
        s = S[d]
        ei = si + di[d]
        ej = sj + dj[d]
        if 0 < ei <= n and 0 < ej <= m:
            sol(ei, ej, cnt+1, word+s, n, m, r, c, k)
            

def solution(n, m, x, y, r, c, k):
    global answer
    
    answer = 'impossible'
    # 이동 횟수와 도착지에 필요한 횟수(홀, 짝)가 다를 경우 제외
    if (abs(r-x) + abs(c-y)) % 2 and not k%2:
        pass
    elif not (abs(r-x) + abs(c-y)) % 2 and k%2:
        pass
    else:
        sol(x, y, 0, '', n, m, r, c, k)
    
    return answer