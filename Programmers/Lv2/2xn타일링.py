# 2xn 타일링 Lv2
# 연습문제

# 1개짜리 타일을 붙이는 것과
# 2개짜리 타일을 붙이는 것
def solution(n):
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 1000000007
    answer = arr[n] % 1000000007
    return answer