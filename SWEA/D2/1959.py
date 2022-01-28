# 두 개의 숫자열

T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split()))
    l_1 = list(map(int, input().split()))
    l_2 = list(map(int, input().split()))
    d = abs(A - B)

    max_sum = 0
    sum = 0

    if A == B:
        for i0 in range(A):
           sum += l_1[i0]*l_2[i0]
        max_sum = sum

    elif A > B:
        for i0 in range(0, d+1):
            for i1 in range(B):
                sum += l_1[i1+i0] * l_2[i1]
            if sum > max_sum:
                max_sum = sum
            sum = 0

    else:
        for i0 in range(0, d+1):
            for i1 in range(A):
                sum += l_1[i1] * l_2[i1+i0]
            if sum > max_sum:
                max_sum = sum
            sum = 0

    print(f'#{i} {max_sum}')
    