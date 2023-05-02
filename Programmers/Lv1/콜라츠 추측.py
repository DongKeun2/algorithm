# 콜라츠 추측 Lv1
# 콜라츠 추측

# 1로 만들기
# 홀수라면 3을 곱하고 1을 더한다
# 짝수라면 2로 나눈다
# 500번 이상 반복시 -1을 반환한다.
def solution(num):
    answer = 0
    while num != 1:
        if answer > 500:
            return -1
        
        if num%2:       
            num *= 3
            num += 1
        else:
            num //= 2

        answer += 1
    return answer