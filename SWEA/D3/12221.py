# 구구단2

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    if a<10 and b<10:
        print(f'#{i} {a*b}')
    else:
        print(f'#{i} -1')