# 미생물 격리

# 방향대로 한 칸 움직이고 약품이 있는 곳이면 반으로 줄이고 방향 바꿔주기
def sol(si, sj, n, d):
    ei = si + di[d]
    ej = sj + dj[d]
    if ei >= N-1 or ei <= 0:
        n //= 2
        d = (d+1)%2
    elif ej >= N-1 or ej <= 0:
        n //= 2
        d = (d+1)%2 + 2
    return [ei, ej, n, d]


T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    mc = []
    for _ in range(K):
        si, sj, n, d = map(int, input().split())
        mc.append([si, sj, n, d-1])

    t = 0
    while M > t:
        # 모든 군집 이동
        for i in range(len(mc)):
            si, sj, n, d = mc[i]
            mc[i] = sol(si, sj, n, d)

        # 빈 군집 없애기
        r = []
        for i in range(len(mc)):
            if mc[i][2] == 0:
                r.append(i)
        for i in r[::-1]:
            mc.pop(i)

        # 이동후 겹친 군집 합치기
        while True:
            flag = 0
            for i in range(len(mc)-1):
                lst = [i]
                for j in range(i+1, len(mc)):
                    if mc[i][0] == mc[j][0] and mc[i][1] == mc[j][1]:
                        lst.append(j)

                # 같은 위치가 2개 이상일 경우
                if len(lst) >= 2:
                    mv = mc[lst[0]][2]
                    mi = lst[0]
                    tot = 0

                    # 가장 큰 위치에 더한 값, 나머지 0 저장
                    for idx in lst:
                        tot += mc[idx][2]
                        if mv < mc[idx][2]:
                            mv = mc[idx][2]
                            mi = idx
                    mc[mi][2] = tot
                    for idx in lst:
                        if mi != idx:
                            mc[idx][2] = 0

                    # 0 저장된 군집 지우기
                    r = []
                    for j in range(len(mc)):
                        if mc[j][2] == 0:
                            r.append(j)
                    for j in r[::-1]:
                        mc.pop(j)

                    # mc의 개수가 바뀌었으므로 다 종료 후 다시 시작
                    flag = 1
                if flag == 1:
                    break
            else:
                flag = -1

            if flag == -1:
                break
        t += 1
    result = 0
    for i in range(len(mc)):
        result += mc[i][2]

    print(f'#{test_case} {result}')