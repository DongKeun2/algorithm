# 2025 프로그래머스 코드챌린지 2차 예선, Lv1

# 완탐, 순서대로 쌓아가면서 계산
def solution(n, w, num):
    lst = [0] * (w+1)
    cnt, t, target, low_num = 1, 1, 0, 0
    flag = 1
    while cnt <= n:
        if cnt == num:
            low_num = lst[t]
            target = t
        lst[t] += 1
        if not cnt % w: flag *= -1
        else: t += flag
        cnt += 1
    return lst[target] - low_num