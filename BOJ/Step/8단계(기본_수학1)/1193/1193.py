# 분수찾기

X = int(input())

if X == 1:
    print('1/1')

else:
    num = 1
    N = 1
    while X > num:
        N += 1
        num += N
    if N % 2 == 0:
        print(f'{N - (num - X)}/{1 + (num - X)}')
    else:
        print(f'{1 + (num - X)}/{N - (num - X)}')

