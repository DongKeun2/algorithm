# 동적계획법(Dynamic Programming) / N으로 표현, lv3

def solution(N, number):
    if number == N: return 1
    # dp[i]는 i개의 N을 사용했을 때 가능한 수의 모음
    ## 1개일 때는 N만 가능
    dp = [[], [N]]
    # 2~8개까지 가능한 모음 찾기
    for cnt in range(2, 9):
        tmp_set = set({int(str(N)*cnt)})
        # 만약 3개의 N으로 만드는 조합을 찾는다면
        ## 1개 조합과 2개 조합을 합쳐서 만들 수 있음, -와 //는 순서도 영향이 있음
        for i in range(1, cnt):
            a, b = i, cnt - i
            for x in dp[a]:
                for y in dp[b]:
                    tmp_set.add(x+y)
                    tmp_set.add(x-y)
                    tmp_set.add(x*y)
                    if y != 0: tmp_set.add(x//y)
        if number in tmp_set: return cnt
        dp.append(list(tmp_set))
    return -1
