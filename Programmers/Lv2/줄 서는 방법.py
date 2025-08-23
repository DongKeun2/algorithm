# 연습문제 / 줄 서는 방법, Lv2

# 팩토리얼 계산 함수
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

def solution(n, k):
    # 1번째 순서로 answer 시작
    answer = [i for i in range(1, n+1)]
    idx = 1
    # idx-1번째 자리부터 맞는 수 배치
    while k > 1 and idx < n:
        flag = factorial(n - idx)
        # k가 flag보다 작으면 idx-1번째 자리 순서가 바뀌지 않음
        if k > flag:
            reminder = k // flag
            if not k % flag: reminder -= 1
            if k % flag: k %= flag
            else: k = flag
            num = answer.pop(idx-1 + reminder)
            answer.insert(idx-1, num)
        # idx-1번째 자리 구한 뒤 다음 수 구하기
        idx += 1
    return answer
