# 구구단1

T = int(input())

nl = [0] * 101

for i in range(1, 10):
    for j in range(1, 10):
        nl[i*j] = 1



for i in range(1, T+1):
    n = int(input())
    if nl[n] == 1:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')
