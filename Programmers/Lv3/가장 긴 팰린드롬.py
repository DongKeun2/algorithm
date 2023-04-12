# 가장 긴 팰린드롬 Lv3
# 연습문제

# 모든 지점에서 양쪽으로 뻗어나가면서 확인
def solution(s):
    answer = 1
    for i in range(len(s)):
        # 팰린드롬의 길이가 홀수인 경우
        l, r = i, i
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        answer = max(answer, r-l-1)
        
        # 팰린드롬의 길이가 짝수인 경우
        l, r = i, i+1
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        answer = max(answer, r-l-1)
    return answer