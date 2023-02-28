# 트리 트리오 중간값 Lv4
# 월간 코드 챌린지 시즌1

from collections import deque

# 끝에서 끝으로 두 번 확인(트리의 양 끝 확인)
# tmp에 각 노드별 트리의 끝에서의 거리 2개 값 저장
def solution(n, edges):
    
    arr = [[] for _ in range(n+1)]
    for s, e in edges:
        arr[s].append(e)
        arr[e].append(s)
    
    # 1번 노드는 항상 있으므로
    # 1번 노드를 통해 가장 끝 노드 ns를 확인
    q = deque([1])
    vst = [0] * (n+1)
    vst[1] = 1
    ns = 0
    while q:
        s = q.popleft()
        if vst[s] > vst[ns]:
            ns = s
        for e in arr[s]:
            if vst[e] == 0:
                vst[e] = vst[s] + 1
                q.append(e)
    
    # ns노드에서 가장 먼 노드인 nns노드 확인
    # 이 과정에서 각 노드별 ns노드와 떨어진 거리 tmp[n][0]에 저장
    tmp = [[0,0] for _ in range(n+1)]
    
    q = deque([ns])
    vst = [0] * (n+1)
    vst[ns] = 1
    nns = 0
    while q:
        s = q.popleft()
        if vst[s] > vst[nns]:
            nns = s
        for e in arr[s]:
            if vst[e] == 0:
                vst[e] = vst[s] + 1
                tmp[e][0] = vst[e]
                q.append(e)
    
    # nns노드에서 각 노드별로 거리 tmp[n][1]에 저장
    q = deque([nns])
    vst = [0] * (n+1)
    vst[nns] = 1
    while q:
        s = q.popleft()
        for e in arr[s]:
            if vst[e] == 0:
                vst[e] = vst[s] + 1
                tmp[e][1] = vst[e]
                q.append(e)
    
    # ns와 nns를 포함한 f(ns, nns, ?)값이 최대
    # 중앙값이므로 ns와 nns 거리가 최대
    # tmp[?] 값 중 큰 값이 중앙값 
    answer = 0
    for i in range(1, n+1):
        if i != ns and i != nns:
            answer = max(answer, max(tmp[i])-1)
    return answer