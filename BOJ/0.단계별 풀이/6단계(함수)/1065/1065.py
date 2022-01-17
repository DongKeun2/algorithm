# 한수

N = int(input())
if N<100:
    print(N)
else:
    s = 99
    for i in range(100,N+1):
        l = i%10
        m = (i%100)//10
        n = i//100
        if (l-m) == (m-n):
            s+=1
    print(s)