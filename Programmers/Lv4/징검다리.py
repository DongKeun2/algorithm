# 징검다리 Lv4
# 이분탐색

import sys
sys.setrecursionlimit(10**6)

# 이분탐색 풀이
def solution(distance, rocks, n):
    def sol(left, right):
        middle = (left+right)//2
        if left >= right:
            return left-1

        # 바위 사이의 거리가 middle 이상을 만족하는지 확인
        x = 0
        cnt = 0
        for i in range(l):
            if rocks[i] - x >= middle:
                x = rocks[i]
            else:
                cnt += 1
                if cnt > n:
                    return sol(left, middle) # 만족하지 못하면 더 짧은 거리로 확인
        return sol(middle+1, right)     # 만족하면 더 긴 거리로 확인
    
    
    rocks.sort()
    rocks.append(distance)
    l = len(rocks)
    answer = sol(0, distance)
    return answer