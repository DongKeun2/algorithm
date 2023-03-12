# 여행경로 Lv3
# 깊이/너비 우선 탐색(DFS/BFS)

import copy

def solution(tickets):
    global answer
    def sol(S, tmp):
        global answer
        if answer:
            return
        
        if len(tmp) > n:
            answer = copy.deepcopy(tmp)
            return

        # 방문할 수 있는 도시면 방문
        # 동일한 티켓을 사용하지 않도록 dct[S]의 index를 vst에 저장하며 확인
        if S in dct:
            for idx, e in enumerate(dct[S]):
                if S in vst:
                    if idx not in vst[S]:
                        vst[S].append(idx)
                        sol(e, tmp + [e])
                        vst[S].pop()
                else:
                    vst[S] = [idx]
                    sol(e, tmp + [e])
                    vst[S].pop()
                
    
    # 각 도시별 티켓 저장
    dct = {}
    for s, e in tickets:
        if s in dct:
            dct[s].append(e)
        else:
            dct[s] = [e]
    
    # 알파벳 순 정렬
    for lst in dct.values():
        lst.sort()
    
    # ICN 도시부터 시작
    n = len(tickets)
    vst = {}
    answer = []
    sol('ICN', ['ICN'])
    return answer