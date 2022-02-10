# 스위치 켜고 끄기

swn = int(input())
sw = list(map(int, input().split()))

sn = int(input())
stl = []
for _ in range(sn):
    stl.append(list(map(int, input().split())))

for st in stl:
    if st[0] == 1:
        cnt = 1
        while ((st[1]*cnt)-1 < swn):
            if sw[st[1]*cnt -1] == 1:
                sw[st[1]*cnt -1] = 0
            else:
                sw[st[1]*cnt -1] = 1
            cnt += 1
    else:
        x=0
        while ((st[1]+x-1) < swn) and ((st[1]-x-1) >= 0):
            if (sw[st[1]+x-1] == sw[st[1]-x-1]):
                x += 1
            else:
                break
        x -= 1
        for i in range(st[1]-x-1, st[1]+x):
            if sw[i] == 1:
                sw[i] = 0
            else:
                sw[i] = 1

if len(sw) > 20:
    res = [sw[i:i+20] for i in range(0, len(sw), 20)]
    for r in res:
        print(' '.join(str(x) for x in r))
else:
    print(' '.join(str(x) for x in sw))
                