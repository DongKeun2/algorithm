# 광물 캐기 Lv2
# 연습문제

# DFS 풀이
dct = {
    'diamond': [1, 5, 25],
    'iron': [1, 1, 5],
    'stone': [1, 1, 1]
}

def solution(picks, minerals):
    global answer
    def sol(now, di, ir, st, idx, tot):
        global answer
        if tot >= answer:
            return
        
        for i in range(idx, idx+5):
            if i >= n:
                answer = min(answer, tot)
                return
            tot += dct[minerals[i]][now]
        
        if not di and not ir and not st:
            answer = min(answer, tot)
            return
        
        if di:
            sol(0, di-1, ir, st, idx+5, tot)
        if ir:
            sol(1, di, ir-1, st, idx+5, tot)
        if st:
            sol(2, di, ir, st-1, idx+5, tot)
        
    answer = 10**18
    n = len(minerals)
    if picks[0]:
        sol(0, picks[0]-1, picks[1], picks[2], 0, 0)
    if picks[1]:
        sol(1, picks[0], picks[1]-1, picks[2], 0, 0)
    if picks[2]:
        sol(2, picks[0], picks[1], picks[2]-1, 0, 0)
    return answer