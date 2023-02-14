# 연습문제 LV2

# 해당 자릿수에서 -하는 경우와 +하는 경우 모두 계산
def sol(n, cnt):
    global answer
    
    if cnt > answer:
        return

    # 0이 되었을 때 소모한 마법의 돌 최솟값 갱신
    if n == 0:
        answer = min(answer,cnt)
        return
    
    sol(n//10, cnt+n%10)
    sol(n + (10-n%10), (cnt + 10-n%10))

# 최댓값 설정
answer = 10**18
def solution(storey):
    global answer
    sol(storey, 0)
    return answer