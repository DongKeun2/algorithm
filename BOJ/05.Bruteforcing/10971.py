# 외판원 순회 2
# 백트래킹, 브루트포스, 외판원 순회

def sol(tot, flag, s):
    global result
    # 여행비가 결과값보다 커지면 더 볼 필요가 없다.
    if tot >= result:
        return

    elif sum(v) == (N-1):
        # 마지막에 첫 출발지로 돌아가지 못하면 없는 경로, so 고려x
        if arr[flag][s] != 0:
            tot += arr[flag][s]
            if result > tot:
                result = tot
        return

    else:
        # 첫 출발지 s로 설정
        # s가 정해지면 flag(출발지)를 바꿔가며 여행 할 수 있는 도시(도착지, i)로 이동
        for i in range(N):
            if flag == -1:
                s = i
                sol(tot, i, s)
            elif v[i] == 0 and arr[flag][i] != 0 and i != s:
                v[i] = 1
                sol(tot+arr[flag][i], i, s)
                v[i] = 0
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0 for _ in range(N)]

result = 10000000
flag = -1
tot = 0
s = -1
sol(tot, flag, s)
print(result)