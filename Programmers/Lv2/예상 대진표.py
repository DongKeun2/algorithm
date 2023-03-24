# 예상 대진표 Lv2
# 2017 팁스타운

# 만날때까지 계산
def solution(n,a,b):
    answer = 1
    while (a+1)//2 != (b+1)//2:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer