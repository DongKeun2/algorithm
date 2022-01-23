# 연월일 달력

T = int(input())

for t in range(1,T+1):
    K = input()
    if 12 >= int(K[4:6]) >= 1:
        if int(K[4:6]) == 2:
            if int(K[6:8]) <= 28:
                print(f'#{t} {K[0:4]}/{K[4:6]}/{K[6:8]}')
            else:
                print(f'#{t} -1')
        elif int(K[6:7]) == (4 or 9 or 11):
            if int(K[6:8]) <= 30:
                print(f'#{t} {K[0:4]}/{K[4:6]}/{K[6:8]}')
            else:
                print(f'#{t} -1')
        else:
            if int(K[6:8]) <= 31:
                print(f'#{t} {K[0:4]}/{K[4:6]}/{K[6:8]}')
            else:
                print(f'#{t} -1')
    else:
        print(f'#{t} -1')
