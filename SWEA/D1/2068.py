# 최대수 구하기

T = int(input())

for i in range(1,T+1):
    num_list = list(map(int, input().split()))
    max_num = 0
    for k in num_list:
        if k >= max_num:
            max_num = k
    print(f'#{i} {max_num}')