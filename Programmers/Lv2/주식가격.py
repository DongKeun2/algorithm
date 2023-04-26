# 주식가격 Lv2
# 스택/큐

# heapq 내림차순 정렬(-활용) 인덱스와 함께 저장
# 값이 떨어진 순간 확인하여 계산
# heapq에 마지막까지 남은 값은 값이 떨어지지 않은 경우
from heapq import heappush, heappop

def solution(prices):
    n = len(prices)
    answer = [0] * n
    h = []
    for i in range(n):
        while h:
            if h[0][0] < -prices[i]:
                _, s = heappop(h)
                answer[s] = i-s
            else:
                break
        heappush(h, (-prices[i], i))
    
    while h:
        _, s = heappop(h)
        answer[s] = n-s-1
    return answer