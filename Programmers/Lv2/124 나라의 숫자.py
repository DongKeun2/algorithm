# 연습문제 / 124 나라의 숫자, Lv2

# 재귀 풀이 => 효율성 1문제 시간초과
## while문으로 수정 후 통과
def solution(n):
    answer = ''
    while n > 0:
        answer = str(int(n) % 3 if int(n)%3 else '4') + answer
        n = (int(n)-1)//3
    # def sol(x):
    #     if int(x) <= 0:
    #         return ''
    #     return sol((int(x)-1)//3) + str(int(x) % 3 if int(x)%3 else '4')
    # answer = sol(str(n))
    return answer