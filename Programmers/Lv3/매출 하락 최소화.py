# 2021 카카오 블라인드 Lv3

import sys
sys.setrecursionlimit(10**6)

# DFS + DP
def solution(sales, links):
    # index 0에 직원번호 x가 워크숍에 가지 않은 경우, 1에 간 경우
    # x의 부하직원들 갱신 후 진행
    def sol(x):
        if arr[x]:
            dp[x][1] = sales[x-1]
            num = 0
            # 참여, 부하직원의 참여 여부 상관없이 최솟값을 더함
            # 미참여, 부하직원 중 최소 한명은 참여한 경우의 최솟값 
            for y in arr[x]:
                sol(y)
                num += min(dp[y])
                dp[x][1] += min(dp[y])
            for y in arr[x]:
                dp[x][0] = min(dp[x][0], num - min(dp[y]) + dp[y][1])
        # 말단 직원의 경우 
        else:
            dp[x][0] = 0
            dp[x][1] = sales[x-1]
        
    n = len(sales)
    arr = [[] for _ in range(n+1)]
    for a, b in links:
        arr[a].append(b)
        
    dp = [[10**18, 10**18] for _ in range(n+1)]
    sol(1)
    answer = min(dp[1])
    
    return answer