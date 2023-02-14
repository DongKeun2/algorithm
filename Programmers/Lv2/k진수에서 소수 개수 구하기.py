# 2022 카카오 블라인드 Lv2

import math

# 10진수 n을 k진수로 변환
def trans(n, k):
    if n < k:
        return str(n)
    return trans(n//k, k) + str(n%k)


# 단일 x에 대해 소수 판별
def is_prime(x):
    if x < 2:
        return False
    else:
        for num in range(2, int(math.sqrt(x)) + 1):
            if x%num == 0:
                return False
        return True
    

def solution(n, k):
    S = trans(n, k)
    lst = S.split('0')
    answer = 0
    for l in lst:
        if l and is_prime(int(l)):
            answer += 1
    return answer