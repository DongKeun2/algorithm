# Calkin-Wilf tree 1

T = int(input())

for i in range(1, T+1):
    s = input()
    a, b = 1, 1
    for k in s:
        if k == 'L':
            b = a+b
        elif k == 'R':
            a = a+b
    
    print(f'#{i} {a} {b}')