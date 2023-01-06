# 계단 오르기

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 2개 이하라면 모두 밟는 것이 최대
if N <= 2:
    print(sum(lst))
else:
    # 밟는 것, 안 밟는 것
    dp1 = [0] * N
    dp2 = [0] * N

    # dp1은 전을 밟거나 안밟은 것(전전것은 밟아야 함)과 비교해서 큰 값을 가져옴
    # dp2는 이전 dp1을 가져옴
    dp1[0] = lst[0]
    dp1[1] = lst[0] + lst[1]
    dp2[1] = lst[0]
    for i in range(2, N):
        dp1[i] = lst[i] + max(dp2[i-1], dp2[i-2]+lst[i-1])
        dp2[i] = dp1[i-1]

    # 마지막 계단을 밟았을 경우의 최댓값 출력
    print(dp1[-1])
