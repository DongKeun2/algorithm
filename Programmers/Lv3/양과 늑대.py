# 2022 카카오 블라인드 Lv3

def solution(info, edges):
    global result
    # 양의 수 answer, 늑대의 수 cnt
    # 현재 방문 정점 vst
    def sol(vst, answer, cnt):
        global result
        
        # 양 최댓값 갱신
        if result < answer:
            result = answer
        
        # 방문한 곳과 연결된 곳 중 아직 방문하지 않은 곳 방문
        for x in vst:
            for e in arr[x]:
                if not e in vst:
                    if info[e]:
                        if answer > cnt+1:
                            sol(vst+[e], answer, cnt+1) # 늑대라면 양의 수가 많을때만 방문
                    else:
                        sol(vst+[e], answer+1, cnt)     # 양이라면 무조건 방문
    
    n = len(info)
    arr = [[] for _ in range(n)]
    for s, e in edges:
        arr[s].append(e)
    
    result = 0
    sol([0], 1, 0)
    return result