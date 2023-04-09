# N개의 최소공배수
# 연습문제

# 최대 공약수
def gcd(n, m):
    if m > n:
        n, m = m, n

    if n%m:
        return gcd(m, n%m)
    return m

# 최소 공배수
def lcm(n, m):
    return n//gcd(n, m) * m

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        y = arr[i]
        answer = lcm(answer, y)
    return answer