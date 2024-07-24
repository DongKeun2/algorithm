# 스택
import sys
input = sys.stdin.readline

N = int(input())

st = []
for _ in range(N):
    x = list(map(str, input().split()))

    if x[0] == 'push':
        st.append(x[1])
    
    elif x[0] == 'pop':
        if st:
            print(st.pop())
        else:
            print(-1)
    
    elif x[0] == 'size':
        print(len(st))
    
    elif x[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)
    
    else:
        if st:
            print(st[len(st)-1])
        else:
            print(-1)
