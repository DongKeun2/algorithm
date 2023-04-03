# 숫자 블록 Lv2
# 연습문제

# 이게 왜 2레벨이냐
import math

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        tmp = 1
        if i == 1:
            tmp = 0
        for j in range(2, int(math.sqrt(i)+1)):
            if i < j:
                tmp = 1
                break
            elif i%j == 0:
                tmp = max(tmp, j if j <= 10000000 else 1, i//j if i//j <= 10000000 else 1)
        answer.append(tmp)
    return answer