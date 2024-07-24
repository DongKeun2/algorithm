# 덱

import sys
input = sys.stdin.readline

N = int(input())

d = []
for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push_front':
        d.insert(0, cmd[1])

    elif cmd[0] == 'push_back':
        d.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if d:
            print(d.pop(0))
        else:
            print(-1)

    elif cmd[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(d))
    
    elif cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    
    elif cmd[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)

    else:
        if d:
            print(d[-1])
        else:
            print(-1)
