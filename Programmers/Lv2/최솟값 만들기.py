# 최솟값 만들기 Lv2
# 연습문제

def solution(A,B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(n):
        answer += A[i]*B[i]

    return answer