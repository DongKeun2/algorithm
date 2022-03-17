# 세제곱근을 찾아라

T = int(input())

temp = [0]*(10**6+1)
for i in range(10**6+1):
    temp[i] = i**3

for test_case in range(1, T+1):
    N = int(input())

    result = -1
    if N in temp:
        result = temp.index(N)

    print(f'#{test_case} {result}')