# 연산자 끼워넣기
# 브루트 포스, 백트래킹

# 브루트 포스 (dfs)
# 계산할 숫자 lst[idx], 현재 진행 num
# 남은 덧셈 뺄셈 곱셈 나눗셉 수 psmd
def sol(idx, num, p, s, m, d):
    global result1, result2

    if idx >= N:
        if result1 < num:
            result1 = num
        if result2 > num:
            result2 = num
        return

    if p > 0:
        sol(idx+1, num+lst[idx], p-1, s, m, d)

    if s > 0:
        sol(idx+1, num-lst[idx], p, s-1, m, d)

    if m > 0:
        sol(idx+1, num*lst[idx], p, s, m-1, d)

    if d > 0:
        if num >= 0:
            sol(idx+1, num//lst[idx], p, s, m, d-1)
        else:
            sol(idx+1, -(abs(num)//lst[idx]), p, s, m, d-1)


N = int(input())
lst = list(map(int, input().split()))
op = list(map(int, input().split()))

result1 = -10**9
result2 = 10**9
sol(1, lst[0], op[0], op[1], op[2], op[3])

print(result1)
print(result2)