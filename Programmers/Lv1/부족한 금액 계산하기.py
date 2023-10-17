# 부족한 금액 계산하기 Lv1
# 위클리 챌린지

def solution(price, money, count):
    answer = 0
    tot = sum(price * i for i in range(1, count+1))
    if tot > money:
        answer = tot - money
    return answer