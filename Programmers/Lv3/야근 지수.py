# 야근 지수 Lv3
# 연습문제

from heapq import heappush, heappop

def solution(n, works):
    h = []
    for w in works:
        heappush(h, -w)
    
    # 큰 수부터 -1씩 해주어 다시 저장
    # 중간에 0이 나온다면 모든 수가 0이므로 야근 지수는 0
    while n > 0:
        s = heappop(h)
        if s >= 0:
            return 0
        heappush(h, s+1)
        n -= 1
    
    # n시간 이후 남은 작업량의 야근 지수 계산
    answer = 0
    for w in h:
        answer += w**2
    return answer