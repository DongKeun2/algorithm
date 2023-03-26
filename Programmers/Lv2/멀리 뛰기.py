# 멀리 뛰기 Lv2
# 연습문제

# n번째 칸에 도달하는 경우의 수
# 1. n-1번째 칸에서 1칸 점프
# 2. n-2번째 칸에서 2칸 점프 
def solution(n):
    answer = 0
    arr = [0] * 2001
    arr[0], arr[1] = 1, 1
    for i in range(2, 2001):
        arr[i] = arr[i-1] + arr[i-2]
    answer = arr[n] % 1234567
    return answer