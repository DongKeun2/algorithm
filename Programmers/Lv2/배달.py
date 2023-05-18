# 배달 Lv2
# Summer/Winter Coding(~2018)

# 힙 활용 다익스트라 풀이 (걸리는 시간, 도착 마을)

# lst에 해당 마을에 배달하는데 걸리는 시간 저장
## 최댓값으로 저장해둔 뒤, 1번부터 갈 수 있는 경로 탐색

# now보다 큰 값이 lst에 저장되어 있다면 now로 갱신
## 연결된 다른 마을로 이동하는 시간 now+t로 재탐색

# K이하 시간이 저장된 마을의 수 반환
from heapq import heappush, heappop

def solution(N, road, K):
    arr = [[] for _ in range(N+1)]
    for a, b, c in road:
        arr[a].append((b, c))
        arr[b].append((a, c))
        
    lst = [10**16] * (N+1)
    lst[1] = 0
    h = []
    for e, t in arr[1]:
        heappush(h, (t, e))
        
    while h:
        now, s = heappop(h)
        if lst[s] > now:
            lst[s] = now
            for e, t in arr[s]:
                heappush(h, (now+t, e))

    answer = 0
    for i in range(1, N+1):
        if lst[i] <= K:
            answer += 1

    return answer