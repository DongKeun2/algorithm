# 월간 코드 챌린지 시즌3

# 규칙찾아서 구현
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        if (i // n) <= (i)%n:
            answer.append((i)%n + 1)
        else:
            answer.append(i//n + 1)
    return answer

# n이 3인 경우 배열, 몫, 나머지
# 1 2 3 2 2 3 3 3 3
# 0 0 0 1 1 1 2 2 2
# 0 1 2 0 1 2 0 1 2