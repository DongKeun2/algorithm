# 큰 놈,작은 놈,같은 놈

T = int(input())
for i in range(1,T+1):
    num_1, num_2 = input().split()
    if num_1 < num_2:
        print(f'#{i} <')
    elif num_1 > num_2:
        print(f'#{i} >')
    else:
        print(f'#{i} =')