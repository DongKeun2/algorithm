# 더 맵게 Lv2
# 힙(Heap)

# 힙 기본 풀이
# K이상만 존재하면 종료 => 연산 횟수 반환
# 힙이 빌때까지 안된다면 실패
from heapq import heappush, heappop

def solution(scoville, K):
    h = []
    for s in scoville:
        heappush(h, s)
        
    cnt = 0
    flag = False
    while h:
        a = heappop(h)
        if a >= K:
            break
        if not h:
            flag = True
            break
            
        b = heappop(h)
        heappush(h, a+b*2)
        cnt += 1
        
    if flag:
        answer = -1
    else:
        answer = cnt
    return answer