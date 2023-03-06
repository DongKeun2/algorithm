# 최고의 집합 Lv3
# 연습문제

def solution(n, s):
    # 모두 1로도 만들 수 없는 경우
    if n > s:
        return [-1]
    
    # 가장 적은 차이로 수를 구성하여 집합을 만든다.
    answer = [s//n] * n
    for i in range(1, s%n+1):
        answer[-i] += 1
    
    return answer