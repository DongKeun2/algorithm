# 수 나누기 게임 / 골드5

N = int(input())
lst = list(map(int, input().split()))

answer = [[0,0] for _ in range(10**6 + 1)]
for i in lst:
    answer[i][0] = 1

for n in lst:
    tmp = n * 2
    while tmp <= 10**6:
        if answer[tmp][0]:
            answer[n][1] += 1
            answer[tmp][1] -= 1
        tmp += n

print(*[answer[m][1] for m in lst])