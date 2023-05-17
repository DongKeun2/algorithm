# 순위 Lv3
# 그래프

# 각 선수별로 이긴 선수 목록 w
# 진 선수 목록 l 생성 및 저장
# deque활용 bfs풀이
# 선수마다 확인하여 본인을 이긴 선수의 수 + 본인에게 진 선수의 수 cnt계산
# cnt값이 n-1이라면 순위를 알 수 있는 선수이다. 
from collections import deque

def solution(n, results):
    w = [[] for _ in range(n+1)]
    l = [[] for _ in range(n+1)]
    for a, b in results:
        w[a].append(b)
        l[b].append(a)
    
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        q1 = deque(w[i])
        q2 = deque(l[i])
        vst1 = [0] * (n+1)
        for w1 in w[i]:
            vst1[w1] = 1
        vst2 = [0] * (n+1)
        for l1 in l[i]:
            vst2[l1] = 1
            
        while q1:
            s1 = q1.popleft()
            cnt += 1
            for e1 in w[s1]:
                if not vst1[e1]:
                    vst1[e1] = 1
                    q1.append(e1)

        while q2:
            s2 = q2.popleft()
            cnt += 1
            for e2 in l[s2]:
                if not vst2[e2]:
                    vst2[e2] = 1
                    q2.append(e2)
                    
        if cnt >= n-1:
            answer += 1
            
    return answer