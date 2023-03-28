# 단어 퍼즐 Lv4
# 2017 팁스타운

# DP풀이
# t를 완성시킬 수 있는 단어를 앞에서부터 탐색
# dp의 해당 인덱스에 단어를 조합해 만들 수 있는 최솟값을 저장
def solution(strs, t):
    n = len(t)
    dp = [10**18] * (n+1)
    dp[0] = 0
    for i in range(n):
        for j in range(1, 6):
            if i + j > n:
                break
            s = t[i:i+j]
            if s in strs:
                dp[i+j] = min(dp[i+j], dp[i] + 1)
    
    answer = dp[-1]
    if answer == 10**18:
        answer = -1
    return answer