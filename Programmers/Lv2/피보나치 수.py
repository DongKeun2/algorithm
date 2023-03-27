# 피보나치 수 Lv2
# 연습문제

def solution(n):
    arr = [0] * 100001
    arr[1] = 1
    for i in range(2, 100001):
        arr[i] = arr[i-1] + arr[i-2]
    answer = arr[n] % 1234567
    return answer