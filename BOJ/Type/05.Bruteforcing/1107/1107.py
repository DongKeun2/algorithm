# 리모컨

N = int(input())
M = int(input())
if M != 0:
    lst = list(map(int, input().split()))

    result = 499900
    for i in range(1000000):
        i = str(i)
        for j in range(len(i)):
            if int(i[j]) in lst:
                break
            if j == len(i)-1:
                result = min(result, abs(int(i) - N) + len(i))    

    result = min(result, abs(N-100))
else:
    result = min(len(str(N)), abs(N-100))
print(result)