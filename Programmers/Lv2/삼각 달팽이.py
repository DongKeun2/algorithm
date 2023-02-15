# 월간 코드 챌린지 시즌1 lv2

# 아래, 오른쪽, 왼쪽 대각선
di = [1, 0, -1]
dj = [0, 1, -1]
def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    
    # 총 cnt까지 num을 1씩 증가시키며 arr에 저장
    cnt = sum(i for i in range(1, n+1)) 
    num = 1
    i = 0
    j = 0
    d = 0
    while num <= cnt:
        arr[i][j] = num
        i += di[d]
        j += dj[d]
        # 채울 수 없는 자리에서 방향 전환
        if i < 0 or i >= n or j < 0 or j > i or arr[i][j]:
            i -= di[d]
            j -= dj[d]
            d = (d+1)%3
            i += di[d]
            j += dj[d]
        num += 1
        
    for lst in arr:
        answer.extend(lst)
    return answer
