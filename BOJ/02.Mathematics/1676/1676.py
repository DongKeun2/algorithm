# 팩토리얼 0의 개수

n = int(input())

nf = 1
for i in range(2, n+1):
    nf *= i

cnt = 0
while nf > 10:
    if nf % 10 == 0:
        cnt += 1
        nf = nf//10
    else:
        break

print(cnt)
