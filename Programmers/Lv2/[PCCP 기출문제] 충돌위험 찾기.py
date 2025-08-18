# [PCCP 기출문제] 3번 / 충돌위험 찾기, Lv2

def solution(points, routes):
    answer = 0
    m = len(routes)
    robots = []
    goal = [[] for _ in range(m)]
    for idx, route in enumerate(routes):
        s, p_lst = route[0], route[1:]
        robots.append(points[s-1][:])
        for p in p_lst: goal[idx].append(points[p-1][:])

    # 0초 떄 충돌위치 확인
    vst = [[0] * 101 for _ in range(101)]
    for r, c in robots:
        if not vst[r][c]: vst[r][c] = 1
        elif vst[r][c] == 1:
            vst[r][c] += 1
            answer += 1

    while True:
        vst = [[0] * 101 for _ in range(101)]
        cnt = 0
        for i in range(m):
            rx, ry = robots[i]
            # 이미 나갔으면 수량체크
            if not len(goal[i]): cnt += 1
            else:
                gx, gy = goal[i][0]
                # 안 나갔으면 위치 이동, 마지막 포인트에 도착했다면 goal 지워주기 
                if rx > gx: robots[i][0] -= 1
                elif rx < gx: robots[i][0] += 1
                elif ry > gy: robots[i][1] -= 1
                elif ry < gy: robots[i][1] += 1
                else: goal[i].pop(0)
                # 중간 포인트라면 바로 지워주기
                if len(goal[i]) > 1 and robots[i][0] == goal[i][0][0] and robots[i][1] == goal[i][0][1]: goal[i].pop(0)

                if len(goal[i]): 
                    if not vst[robots[i][0]][robots[i][1]]: vst[robots[i][0]][robots[i][1]] = 1
                    else:
                        if vst[robots[i][0]][robots[i][1]] == 1:
                            answer += 1
                            vst[robots[i][0]][robots[i][1]] = vst[robots[i][0]][robots[i][1]] + 1
        if cnt >= m: return answer