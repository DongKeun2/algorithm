# 월간 코드 챌린지 시즌1 Lv2

# 0제거 전 후 비교로 제거된 0의 수 세기
# 제거 후 문자열 길이를 2진수 변환
# 1이 될때까지 반복
def solution(s):
    cnt = 0
    zero_num = 0
    while True:
        if s == "1":
            break
        n = len(s)
        s = ''.join(s.split('0'))
        m = len(s)
        zero_num += n - m
        cnt += 1
        
        s = bin(m).lstrip('0b')
    answer = [cnt, zero_num]
    return answer