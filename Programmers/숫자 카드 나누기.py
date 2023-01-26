# 숫자 카드 나누기

# n,m의 최대공약수(유클리드 호제법) 반환
def gcd(n, m):
    if n < m:
        n, m = m, n
        
    if n%m == 0:
        return m
    return gcd(m, n%m)


# 리스트의 최대공약수 반환
def sol(lst):
    if len(lst) == 1:
        return lst[0]
    
    value = gcd(lst[0], lst[1])
    
    if len(lst) > 2:
        for num in lst[2:]:
            value = gcd(num, value)
    
    return value
        

def solution(arrayA, arrayB):
    answer = 0
    # 두 리스트의 최대공약수 구하기
    a = sol(arrayA)
    b = sol(arrayB)
    
    # 1번 조건 확인
    for x in arrayB:
        if not x % a:
            break
    else:
        answer = max(answer, a)    
    
    # 2번 조건 확인
    for y in arrayA:
        if not y % b:
            break
    else:
        answer = max(answer, b)

    
    return answer