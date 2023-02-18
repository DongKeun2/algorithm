#[21년 재직자 대회 예선] 회의실 예약 Lv2

import sys
input = sys.stdin.readline

# 딕셔너리에 회의실 : 9시부터 18시 예약여부 리스트로 저장
N, M = map(int, input().split())
dct = {}
for _ in range(N):
    ln = input().strip()
    dct[ln] = [0]*9

for _ in range(M):
    r, s, t = input().split()
    for i in range(int(s)-9, int(t)-9):
        dct[r][i] = 1

# 회의실마다 몇 개의 예약이 가능한 지 계산
# 각 예약 가능 시간 출력 
cnt = 0
for key in sorted(dct.keys()):
    cnt += 1
    print('Room {}:'.format(key))
    
    st = -1
    flag = 0
    lst = []
    for i in range(9):
        if not flag and dct[key][i] == 0:
            flag = 1
            st = i
        if flag and dct[key][i]:
            flag = 0
            lst.append((st+9, i+9))
            
    if flag:
        lst.append((st+9, 18))

    if lst:
        print('{} available:'.format(len(lst)))
        for st, et in lst:
            if st == 9:
                st = '09'
            print('{}-{}'.format(st, et))
    else:
        print('Not available')
    
    if cnt < N:
        print('-----')