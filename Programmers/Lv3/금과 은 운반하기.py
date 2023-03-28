# 금과 은 운반하기 Lv3
# 월간 코드 챌린지 시즌3

# 이분탐색 풀이
# 해당 시간마다 각 도시의 금, 은, 전체의 최댓값을 운반
# 모든 도시를 운반한 뒤 조건에 맞는 지 확인
def solution(a, b, g, s, w, t):
    n = len(g)
    l = 0
    r = (10**9) * (10**5) * 3
    while l < r:
        m = (l + r) // 2
        gt = 0
        st = 0
        tot = 0
        for i in range(n):
            cnt = m // (t[i]*2) if m % (t[i]*2) < t[i] else m // (t[i]*2) + 1
            gt += g[i] if g[i] <= cnt * w[i] else cnt * w[i]
            st += s[i] if s[i] <= cnt * w[i] else cnt * w[i]
            tot += g[i] + s[i] if g[i] + s[i] <= cnt * w[i] else cnt * w[i]
        
        if gt >= a and st >= b and tot >= a+b:
            r = m
        else:
            l = m+1
    answer = l
    return answer