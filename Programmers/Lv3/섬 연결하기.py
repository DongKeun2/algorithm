# 섬 연결하기 Lv3
# 탐욕법(Greedy)

# 최소 스패닝 트리 (MST)풀이
# Heap활용 Prim알고리즘
from heapq import heappush, heappop

def solution(n, costs):
    arr = [[] for _ in range(n)]
    for s, e, c in costs:
        arr[s].append((c, e))
        arr[e].append((c, s))
        
    h = []
    for c, e in arr[0]:
        heappush(h, (c, e))
    
    answer = 0
    vst = [0] * n
    vst[0] = 1
    while h:
        c, e = heappop(h)
        if not vst[e]:
            vst[e] = 1
            answer += c
            for c, s in arr[e]:
                heappush(h, (c, s))
    return answer