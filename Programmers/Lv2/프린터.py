# 프린터 Lv2
# 스택/큐


# Queue 활용 풀이
from collections import deque

def solution(priorities, location):
    answer = []
    n = len(priorities)
    
    q = deque([])
    for i in range(n):
        q.append((priorities[i], i))
    
    while q:
        num, i = q.popleft()
        for p, _ in q:
            if p > num:
                q.append((num, i))
                break
        else:
            answer.append(i)
            
    for i in range(n):
        if answer[i] == location:
            return i+1
    return answer