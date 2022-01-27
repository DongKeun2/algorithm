
T = int(input())

for i in range(1, T+1):

    N = list(map(int, input().split()))

    N.sort()

    N_sum = sum(N[1:-1])

    print(f'#{i} {round(N_sum/(len(N)-2))}')