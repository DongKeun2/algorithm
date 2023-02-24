# 고고학 최고의 발견 Lv3
# 연습문제

import copy
from itertools import product

di = [0, 1, 0, -1, 0]
dj = [0, 0, 1, 0, -1]
def solution(clockHands):
    global answer
    
    def sol(idx, tmp, turn, cnt):
        global answer

        if cnt > answer:
            return 
        
        # idx 줄 turn에 따라 돌리기
        for j in range(n):
            for d in range(5):
                ei = idx + di[d]
                ej = j + dj[d]
                if 0 <= ei < n and 0 <= ej < n:
                    tmp[ei][ej] = (tmp[ei][ej] + turn[j])%4
        # 마지막 줄이라면 확인 후 출력
        if idx >= n-1:
            for x in tmp:
                if sum(x):
                    return
            answer = min(answer, cnt)
            return
        
        # idx줄 확인 후 다음 turn 구성
        next_turn = [(4-tmp[idx][j])%4 for j in range(n)]
        sol(idx+1, tmp, next_turn, cnt+sum(next_turn))
    
    
    n = len(clockHands)
    answer = 10**18
    for lst in product([i for i in range(4)], repeat=n):
        arr = copy.deepcopy(clockHands)
        sol(0, arr, lst, sum(lst))
    return answer

