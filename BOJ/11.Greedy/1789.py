# 수들의 합
# 수학, 그리디

S = int(input())

n = 1
result = 1
while S >= n:
    result += 1
    n += result

print(result - 1)