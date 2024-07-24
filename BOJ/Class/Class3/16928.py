# 뱀과 사다리 게임, 골드5

N, M = map(int, input().split())

def sol(start, cnt):
    global answer, t
    if cnt > answer or lst[start] <= cnt: return
    if start >= 100:
        answer = min(answer, cnt)
        return
    
    lst[start] = cnt
    for i in range(1, 7):
        if start in ladder:
            sol(ladder[start], cnt)
        elif start in snake:
            sol(snake[start], cnt)
        elif start + i <= 100:
            sol(start+i, cnt+1)
            

ladder = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

snake = {}
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

lst = [10**9] * 101
answer = 10**9
sol(1, 0)
print(answer)