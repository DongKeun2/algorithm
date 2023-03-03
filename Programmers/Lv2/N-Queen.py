# N-Queen Lv2
# 연습문제

def solution(n):
    global answer
    def sol(vst, idx):
        global answer
        if idx >= n:
            answer += 1
            return
        
        # 현재 채워야 할 idx번째 가로줄
        # 이미 채워진 vst[i]의 값에 따라 채울 수 없는 곳 확인 
        tmp = [0]*n
        for i in range(len(vst)):
            tmp[vst[i]] = 1
            x = vst[i] - (idx-i)
            y = vst[i] + (idx-i)
            if 0 <= x:
                tmp[x] = 1
            if y < n:
                tmp[y] = 1

        for i in range(n):
            if tmp[i] == 0:
                sol(vst+[i], idx+1)

    answer = 0
    sol([], 0)
    return answer
