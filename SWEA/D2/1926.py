# 간단한 369게임

N = int(input())

for i in range(1, N+1):
    list_N = []
    n = str(i)
    for j in n:
        list_N.append(j)
    if '3' in list_N or '6' in list_N or '9' in list_N:
        for k in list_N:
            if k == '3' or k == '6'or k == '9':
                print('-', end = '')
        print(' ', end = '')
    else:
        print(i, end = ' ')
