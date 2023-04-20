# 두 원 사이의 정수 쌍 Lv2
# 연습문제

import math

# x=1부터 r2까지 확인
# 각 x좌표마다 y2 <= y <= y1 를 만족하는 y의 개수 * 4
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        y1 = int(math.sqrt(r2**2-x**2))
        y2 = math.ceil(math.sqrt(r1**2-x**2)) if r1 > x else 0
        answer += (y1-y2+1) *4
    return answer
