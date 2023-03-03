# 덧칠하기 Lv2
# 연습문제

# lst에 페인트를 다시 칠해야하는 구역의 값을 0으로 세팅
def solution(n, m, section):
    lst = [1] * (n+1)
    for s in section:
        lst[s] = 0
    
    # idx를 1부터 구역의 끝까지 확인
    # lst[idx] == 0 이라면 idx를 시작지점으로 페인트칠
    answer = 0
    idx = 1
    while n >= idx:
        if lst[idx] == 0:
            answer += 1
            idx += m
        else:
            idx += 1
    return answer