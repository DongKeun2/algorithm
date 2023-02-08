# 2022 카카오 테크 인턴십 Lv3

from heapq import heappush, heappop

# 다익스트라로 풀이
def solution(n, paths, gates, summits):
    global number, intensity
    def sol(x):
        global number, intensity
        vst = [0] * (n+1)
        for k in gates:
            vst[k] = 1
        q = []
        for y, t in arr[x]:
            heappush(q, (t, y))
        
        # intensity가 작은곳부터 연결하며 확인
        tmp = 0
        while q:
            t, e = heappop(q)
            if vst[e] == 0:
                vst[e] = 1
                tmp = max(tmp, t)
                # 연결된 곳이 산봉우리라면 가장 작은 intensity 저장
                # intensity가 같다면 빠른 번호의 산봉우리 저장
                if e in summits:
                    if tmp == intensity:
                        number = min(number, e)
                        return
                    if tmp < intensity:
                        number = e
                        intensity = tmp
                    return
                for s, st in arr[e]:
                    heappush(q, (st, s))
    
    arr = [[] for _ in range(n+1)]
    for s, e, t in paths:
        arr[s].append((e, t))
        arr[e].append((s, t))
    
    number = 0
    intensity = 10**18
    for x in gates:
        sol(x)
    answer = [number, intensity]
    return answer