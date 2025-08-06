# 2025 프로그래머스 코드챌린지 2차 예선

# 그리디 풀이, 서버가 감당이 안 될 때 필요한 만큼만 증설
def solution(players, m, k):
    answer = 0
    lst = [0] * len(players)
    for i in range(len(players)):
        if players[i] >= (lst[i]+1) * m:
            pre = lst[i]
            max_n = 1
            for j in range(i, i+k):
                n = players[i] // m
                if max_n < n: max_n = n
                if j < len(players): lst[j] += n - pre
            answer += max_n - pre
    return answer