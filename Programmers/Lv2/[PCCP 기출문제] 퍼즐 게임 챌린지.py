# PCCP기출문제 2번 / 퍼즐 게임 챌린지,Lv2

def solution(diffs, times, limit):
    n = len(diffs)
    def get_time_for_sol(level):
        t = times[0]
        for i in range(1, n):
            if t > limit: return False
            if level >= diffs[i]: t += times[i]
            else: t += (times[i] + times[i-1])*(diffs[i] - level) + times[i]
        if t > limit: return False
        return True
    
    # 레벨의 최소, 최댓값
    l, r = 1, 100000
    while l < r:
        m = (r+l)//2
        if get_time_for_sol(m): r = m
        else: l = m+1
    return l