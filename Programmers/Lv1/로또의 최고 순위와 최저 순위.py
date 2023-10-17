# 로또의 최고 순위와 최저 순위 lv1
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(lottos, win_nums):
    answer = [0, 0]
    zero_cnt = lottos.count(0)
    cnt = 0
    for lotto in lottos:
        if lotto and lotto in win_nums:
            cnt += 1
    if cnt < 2:
        answer[1] = 6
    else:
        answer[1] = 7 - cnt
    
    if cnt + zero_cnt < 2:
        answer[0] = 6
    else:
        answer[0] = 7 - cnt - zero_cnt
    return answer