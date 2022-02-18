# 농작물 수확하기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]


    if N == 1:
        result = arr[0][0]

    else:
        result = 0 
        for i in range(N//2):
            for j in range(N//2-i,N//2+i+1):
                result += int(arr[i][j])

        for i in range(N//2+1):    
            for j in range(i, N-i):
                result += int(arr[i+N//2][j])

    print(f'#{test_case} {result}')