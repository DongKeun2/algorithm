# 수 이어 쓰기 1

N = int(input())

result = 0
x = 10
cnt = 1
n = 0
while N >= x:
    result += (x-1-(x//10-1))*cnt
    cnt += 1
    x *= 10
x //= 10
result += (N-(x-1))*cnt

print(result)
