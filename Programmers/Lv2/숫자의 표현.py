# 숫자의 표현 Lv2
# 연습문제

# n을 연속한 수의 합으로 표현할 수 있는 방법은
# n의 약수가 홀수라면 가능하다.  
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0 and i%2:
            answer += 1
    return answer