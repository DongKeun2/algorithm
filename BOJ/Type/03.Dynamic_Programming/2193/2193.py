# 이친수

nl = [0 for _ in range(91)]
nl[1] = 1

for i in range(2,91):
    nl[i] = nl[i-1] + nl[i-2]
        

n = int(input())

print(nl[n])