# 그래프 Lv3

from collections import deque

# bfs 풀이, 최댓값의 개수 확인
def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    for s, e in edge:
        arr[s].append(e)
        arr[e].append(s)
        
    q = deque([1])
    vst = [-1] * (n+1)
    vst[1] = 0
    cnt = 0
    answer = 0
    while q:
        s = q.popleft()
        n = vst[s]
        if cnt == n:
            answer += 1
        elif n > cnt:
            cnt = n
            answer = 1
            
        for e in arr[s]:
            if vst[e] == -1:
                vst[e] = n + 1
                q.append(e)
                
    return answer