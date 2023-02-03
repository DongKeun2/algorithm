# 연습문제 LV3

def solution(n, roads, sources, destination):
    answer = []
    # 지역 연결
    arr = [[] for _ in range(100001)]
    for a, b in roads:
        arr[a].append(b)
        arr[b].append(a)
    
    # 시작 지점 0, 나머지 -1로 초기화
    vst = [-1] * (n+1)
    vst[destination] = 0

    # bfs, 연결된 곳 중 방문하지 않은곳마다 해당 시작지점 + 1 저장 후 q에 추가
    q = [destination]
    while q:
        s = q.pop(0)
        for e in arr[s]:
            if vst[e] == -1:
                vst[e] = vst[s] + 1
                q.append(e)

    # 부대원마다 거리 저장 후 출력
    for source in sources:
        answer.append(vst[source])
    
    return answer