# 다음 큰 숫자 Lv2
# 연습문제

# Greedy 풀이
# 주어진 n의 2진수 1의 개수 req
# n ++ 하며 1의 개수 cnt 계산
def solution(n):
    req = 0
    for s in bin(n).lstrip('0b'):
        if s == '1':
            req += 1
    
    while True:
        n += 1
        cnt = 0
        for s in bin(n).lstrip('0b'):
            if s == '1':
                cnt += 1
                if cnt > req:
                    break
        if cnt == req:
            answer = n
            break
        
    return answer