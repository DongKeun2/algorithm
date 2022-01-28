# 간단한 소인수분해

T = int(input())

for i in range(1, T+1):
    N = int(input())

    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0

    while N % 2 == 0:
        cnt_2 += 1
        N = N//2
    
    while N % 3 == 0:
        cnt_3 += 1
        N = N//3

    while N % 5 == 0:
        cnt_5 += 1
        N = N//5

    while N % 7 == 0:
        cnt_7 += 1
        N = N//7

    while N % 11 == 0:
        cnt_11 += 1
        N = N//11

    print(f'#{i} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')