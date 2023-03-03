# 디펜스 게임 Lv2
# 연습문제

from heapq import heappush, heappop

# 막을 수 없는 경우에 이 전 라운드 중 가장 크게 막은 곳에 무적권 사용
def solution(n, k, enemy):
    answer = 0
    h = []
    for e in enemy:
        heappush(h, -e)
        n -= e
        if n < 0:
            k -= 1
            if k < 0:
                break
            n -= heappop(h)
            if n < 0:
                break
        answer += 1
        
    return answer