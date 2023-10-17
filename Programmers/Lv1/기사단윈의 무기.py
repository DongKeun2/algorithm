# 기사단원의 무기 Lv1
# 연습문제

def solution(number, limit, power):
    def sol(n):
        if n == 1: return 1
        cnt = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cnt += 1
                if n // i != i:
                    cnt += 1
        return cnt
    
    answer = 0
    for n in range(1, number+1):
        tmp = sol(n)
        answer += power if tmp > limit else tmp
    return answer