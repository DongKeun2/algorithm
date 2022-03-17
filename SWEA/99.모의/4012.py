# 요리사

# 두 손님의 맛 차이 계산
def sol(lst1, lst2):
    global result

    # 첫 손님의 음식 맛
    tot1 = 0
    for i in lst1:
        for j in lst1:
            if i != j:
                tot1 += S[i][j]

    # 다음 손님의 음식 맛
    tot2 = 0
    for i in lst2:
        for j in lst2:
            if i != j:
                tot2 += S[i][j]

    # 결과값 갱신
    if result > abs(tot1-tot2):
        result = abs(tot1-tot2)
    return


# 두 명의 손님에게 제공할 음식 명단 고르기
def food(lst, idx):
    lst0 = [x for x in lst]

    # 한 손님에게 제공할 음식이 전체 음식의 절반일 때
    # 다른 손님에게 제공할 음식 명단을 만들고 sol함수로 보냄
    if len(lst0) == N//2:
        lst1 = [x for x in lst]
        lst2 = []
        for i in range(N):
            if f[i] not in lst1:
                lst2.append(f[i])
        sol(lst1, lst2)

    elif idx >= N:
        return

    else:
        food(lst0, idx+1)
        lst0.append(f[idx])
        food(lst0, idx+1)
    return


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 음식의 종류
    f = [i for i in range(N)]

    # 첫 손님에게 0번 음식 고정
    lst = [0]
    result = 20000
    food(lst, 1)

    print(f'#{test_case} {result}')