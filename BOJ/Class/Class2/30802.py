# 웰컴 키트, 브론즈3

N = int(input())
lst =  list(map(int, input().split()))
T, P = map(int, input().split())

answer = 0
for x in lst:
    answer += x//T
    if x%T: answer += 1

print(answer)
print(sum(lst)//P, sum(lst)%P)