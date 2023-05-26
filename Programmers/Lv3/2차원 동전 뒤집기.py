# 2차원 동전 뒤집기 Lv3
# 연습문제

# 첫 번째 행을 통해 뒤집을 열을 결정한 뒤 계산
## 첫 번째 행을 뒤집은 경우, 뒤집지 않은 경우 고려
## tmp1과 tmp2를 통해 뒤집을 열의 인덱스 계산

# 다음 행에서 tmp를 확인하며 가능한지 확인
## tmp에 해당하는 열을 뒤집었다고 가정하고 일치하는지 확인
## 정확히 일치 또는 정확히 불일치한다면 다음 행 확인
### 불일치할 시 해당 행을 한 번 더 뒤집는다. / cnt ++

def solution(beginning, target):
    global answer
    def sol(idx, cnt, tmp):
        global answer
        
        if answer <= cnt:
            return
        
        if idx >= n:
            answer = min(answer, cnt)
            return
        
        flag = 0
        for j in range(m):
            if tmp[j] and beginning[idx][j] == target[idx][j]: 
                flag += 1
            elif not tmp[j] and beginning[idx][j] != target[idx][j]:
                flag += 1
                
        if flag >= m:
            sol(idx+1, cnt+1, tmp)
        elif flag <= 0:
            sol(idx+1, cnt, tmp)
        
    n = len(beginning)
    m = len(beginning[0])
    # 첫 번째 행만 확인, 뒤집을 열을 미리 결정한다.
    tmp1 = [0] * m
    tmp2 = [0] * m
    for j in range(m):
        # 첫 번째 행을 뒤집은 경우
        if beginning[0][j] == target[0][j]:
            tmp1[j] = 1
    
        # 첫 번쨰 행을 뒤집지 않은 경우
        if beginning[0][j] != target[0][j]:
            tmp2[j] = 1
    
    answer = 10**18
    sol(1, sum(tmp1)+1, tmp1)
    sol(1, sum(tmp2), tmp2)
    
    if answer == 10**18:
        answer = -1
    return answer