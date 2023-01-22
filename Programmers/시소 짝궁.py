# 코테 연습문제
# Lv2

import sys
sys.setrecursionlimit(10**6)

# 중복 조합 수 계산
def sol(n):
    if n == 2:
        return 1
    return (n-1) + sol(n-1)

def solution(weights):
    answer = 0
    tmp = [0] * 1001
    
    for weight in weights:
        tmp[weight] += 1

    # 100부터 1000까지 확인하므로 큰 수만 확인해주면 된다.
    for i in range(len(tmp)):
        # 중복의 경우
        if tmp[i] >=2:
            answer += sol(tmp[i])
            
        # 3배와 2배가 같은 경우
        if i%2 == 0 and i*3//2 <= 1000 and tmp[i*3//2]:
            answer += tmp[i] * tmp[i*3//2]
        
        # 4배와 2배가 같은 경우
        if i*2 <= 1000 and tmp[i*2]:
            answer += tmp[i] * tmp[i*2]
        
        # 4배와 3배가 같은 경우
        if (i*4)%3 == 0 and i*4//3 <= 1000 and tmp[i*4//3]:
            answer += tmp[i] * tmp[i*4//3]
            
    return answer