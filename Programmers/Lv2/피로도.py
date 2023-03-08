# 피로도 Lv2
# 완전 탐색

def solution(k, dungeons):
    global answer
    # cnt : 탐험한 던전 수
    # tot : 남은 피로도
    # tmp : 탐험한 던전 목록
    def sol(cnt, tot, tmp):
        global answer
        answer = max(answer, cnt)
        
        for i in range(n):
            if i not in tmp and tot >= dungeons[i][0]:
                sol(cnt+1, tot - dungeons[i][1], tmp + [i])
    
    
    answer = 0
    n = len(dungeons)
    for i in range(n):
        if k >= dungeons[i][0]:
            sol(1, k - dungeons[i][1], [i])
    return answer