# 합승 택시 요금 Lv3
# 2021 KAKAO BLIND RECRUITMENT

from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    # x에서 시작하여 모든 지점까지의 최소 요금 저장
    def sol(x, xl):
        h = [(0, x)]
        while h:
            sm, s = heappop(h)
            if xl[s] > sm:
                xl[s] = sm
                for e, em in arr[s]:
                    if xl[e] > sm + em:
                        heappush(h, (sm + em, e))

    arr = [[] for _ in range(n+1)]
    for i, j, m in fares:
        arr[i].append((j, m))
        arr[j].append((i, m))
        
    # a, b, s에서 다익스트라
    al = [10**18] * (n+1)
    bl = [10**18] * (n+1)
    sl = [10**18] * (n+1)
    for x, xl in [(a,al), (b, bl), (s, sl)]:
        sol(x, xl)
    
    # 각 지점별 요금 계산
    answer = 10**18
    for i in range(1, n+1):
        answer = min(answer, al[i] + bl[i] + sl[i])
    return answer