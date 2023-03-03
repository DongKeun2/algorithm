# 3 x n 타일링 Lv2
# 연습문제

def solution(n):
    lst = [0] * (n+1)
    lst[2] = 3
    lst[4] = 11
    # i-2타일의 뒤에 2개짜리 타일을 붙인다.
    ## +(3*lst[i-2])
    # 앞에 2개짜리 타일을 붙인다.(뒤에 붙이는 경우와 겹치는 부분 제외)
    ## -(lst[i-2] - lst[i-4] + 2)
    # 새로 생기는 모양 2개를 더한다. +2
    for i in range(6, n+1, 2):
        lst[i] = 4 * lst[i-2] % 1000000007 - lst[i-4] % 1000000007
    answer = lst[n] % 1000000007
    return answer