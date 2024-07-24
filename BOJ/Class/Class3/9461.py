# 파도반 수열, 실버3

T = int(input())

answer = [0] * 101
answer[1], answer[2], answer[3], answer[4], answer[5] = 1, 1, 1, 2, 2
for i in range(5, 101):
    answer[i] = answer[i-1] + answer[i-5]

for _ in range(T):
    N = int(input())
    print(answer[N])