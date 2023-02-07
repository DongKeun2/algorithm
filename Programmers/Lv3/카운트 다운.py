# 연습문제 Lv3

def solution(target):
    dp = [(10**18, 10**18)] * 100001
    
    # 알고 있는 값 미리 저장
    dp[50] = (1, 1)
    for i in range(1, 21):
        dp[i] = (1, 1)
        dp[i*2] = (1, 0)
        dp[i*3] = (1, 0)
    
    # 이 후 값 dp계산
    # 횟수 최소, 싱글 또는 불 최대 sorted로 정렬
    for i in range(21, 100001):
        if i - 50 > 0:
            dp[i] = sorted((dp[i], (dp[i-50][0]+1, dp[i-50][1]+1)), key = lambda x : (x[0], -x[1]))[0]
        for j in range(1, 21):
            dp[i] = sorted((dp[i], (dp[i-j][0]+1, dp[i-j][1]+1)) , key = lambda x : (x[0], -x[1]))[0]
            if i - j*2 > 0:
                dp[i] = sorted((dp[i], (dp[i-j*2][0]+1, dp[i-j*2][1])), key = lambda x : (x[0], -x[1]))[0]
            if i - j*3 > 0:
                dp[i] = sorted((dp[i], (dp[i-j*3][0]+1, dp[i-j*3][1])), key = lambda x : (x[0], -x[1]))[0]         
        
    answer = dp[target]
    return answer