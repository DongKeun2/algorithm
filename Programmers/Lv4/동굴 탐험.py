# 동굴 탐험 Lv4
# 2020 카카오 인턴십

from collections import deque

def solution(n, path, order):
    arr = [[] for _ in range(n)]
    for s, e in path:
        arr[s].append(e)
        arr[e].append(s)
        
    rep = [0] * n
    for s, e in order:
        rep[e] = s
    
    # 0부터 시작을 못 하므로 예외처리
    if rep[0]:
        return False
    
    # BFS로 방문
    # 방문할 수 없는 곳은 dct에 저장
    # 조건 만족으로 방문이 가능해지면 꺼내서 q에 저장
    q = deque([0])
    vst = [0] * n
    vst[0] = 1
    dct = {}
    while q:
        s = q.popleft()
        if s in dct:
            vst[dct[s]] = 1
            q.append(dct[s])
        for e in arr[s]:
            if not vst[e]:
                if vst[rep[e]]:
                    vst[e] = 1
                    q.append(e)
                else:
                    dct[rep[e]] = e
    
    # 모든 곳을 방문했다면 성공
    answer = False
    if sum(vst) == n:
        answer = True
    return answer