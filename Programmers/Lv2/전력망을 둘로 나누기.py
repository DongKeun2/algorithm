# 연습문제 Lv2

from collections import deque

def solution(n, wires):
    global answer
    # 해당 전선이 끊어져있다는 가정하에 BFS로 1에 연결된 개수 cnt 계산
    # 두 집합의 개수 차이 최소로 갱신
    def sol(x, y):
        global answer
        q = deque([1])
        vst = [0] * (n+1)
        vst[1] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for e in arr[s]:
                if not (s == x and e == y) and not (s == y and e == x) and vst[e] == 0:
                    vst[e] = 1
                    cnt += 1
                    q.append(e)
        answer = min(answer, abs(2*cnt - n))
    
    # 연결
    arr = [[] for _ in range(n+1)]
    for s, e in wires:
        arr[s].append(e)
        arr[e].append(s)
    
    # 최댓값 설정, 모든 전선에 대해 탐색
    answer = 10**18
    for x, y in wires:
        sol(x, y)
    return answer