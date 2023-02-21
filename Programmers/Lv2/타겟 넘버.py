# 타겟 넘버 Lv2
# 깊이/너비 우선탐색(DFS/BFS)

# dfs 풀이
def solution(numbers, target):
    global answer
    def sol(idx, cnt):
        global answer
        if idx >= n:
            if cnt == target:
                answer += 1
            return
        sol(idx+1, cnt + numbers[idx])
        sol(idx+1, cnt - numbers[idx])
    
    
    n = len(numbers)
    answer = 0
    sol(0, 0)
    return answer