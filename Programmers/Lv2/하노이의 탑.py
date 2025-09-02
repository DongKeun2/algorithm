# 연습문제 / 하노이의 탑, Lv2

# 재귀 연습

# 1 - 1, [1 3]
# 2 - 3, [1 2] [1 3] [2 3]
# 3 - 7, [1 3] [1 2] [3 2] [1 3] [2 1] [2 3] [1 3]
# 4 - 15, [1 2] [1 3] [2 3] [1 2] [3 1] [3 2] [1 2] [1 3] [2 3] [2 1] [3 1] [2 3] [1 2] [1 3] [2 3] 


def solution(n):
    answer = []
    def move(size, s, e):
        if size == 1: return answer.append([s, e])
        next = 6 - (s + e)
        move(size-1, s, next)
        answer.append([s, e])
        move(size-1, next, e)
    move(n, 1, 3)
    return answer
