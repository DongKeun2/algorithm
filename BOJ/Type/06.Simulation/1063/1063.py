# 킹
# 구현 시뮬레이션

# 위치를 구하기 위한 딕셔너리 생성
trans = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7
}


# 커맨드 딕셔너리 생성
command = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (-1, 0),
    'T' : (1, 0),
    'RT' : (1, 1),
    'LT' : (1, -1),
    'RB' : (-1, 1),
    'LB' : (-1, -1)
}

# 위치 입력
a, b, N = input().split()

# 위치를 바꿔줌 ex) A2 => 1, 0 / B2 => 1, 1
# ai, aj는 킹의 위치 / bi, bj는 돌의 위치 
ai = int(a[1])-1
aj = trans.get(a[0])

bi = int(b[1])-1
bj = trans.get(b[0])

# N만큼 명령입력
for _ in range(int(N)):

    # 입력받은 명령을 바꿔줌
    c = input()
    di = command.get(c)[0]
    dj = command.get(c)[1]

    # 갈 수 있는 곳이면 킹 옮기기
    if 0 <= ai+di < 8 and 0 <= aj+dj < 8:
        ai += di
        aj += dj

        # 돌의 위치에 킹이 도착하면 돌도 이동 / 못하면 킹 이동 취소
        if ai == bi and aj == bj:
             if 0 <= bi + di < 8 and 0 <= bj + dj < 8:
                 bi += di
                 bj += dj
             else:
                 ai -= di
                 aj -= dj

# 딕셔너리 뒤집고 최종 위치 변환 후 출력
trans2 = {}
for k, v in trans.items():
    trans2[v] = k

a = trans2.get(aj) + str(ai+1)
b = trans2.get(bj) + str(bi+1)

print(a)
print(b)