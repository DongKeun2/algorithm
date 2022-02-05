# -2진수

num = int(input())

if num == 0:
    print(0)

elif num > 0:
    com = 1
    n = 2
    cnt = 1
    while com < num:
        com += 2**n
        n += 2
        cnt += 2

    x = 2**(cnt-1)
    rl = [1]
    for i in range(0, cnt-1)[::-1]:
        if i%2:
            min_x = (-2)**i
            max_x = (-2)**i
            for idx in range(i):
                if idx%2:
                    min_x += (-2)**idx
                else:
                    max_x += 2**idx
                    
            if min_x <= (num - x) <= max_x :
                x -= 2**i
                rl.append(1)
            else:
                rl.append(0)

        else:
            min_x = 2**i
            max_x = 2**i
            for idx in range(i):
                if idx%2:
                    min_x += (-2)**idx
                else:
                    max_x += 2**idx
        
            if min_x <= (num - x) <= max_x:
                x += 2**i
                rl.append(1)
            else:
                rl.append(0)

    print(''.join(str(k) for k in rl))


elif num < 0:
    com = -2
    n = 3
    cnt = 2
    while com > num:
        com -= 2**n
        n += 2
        cnt += 2
    
    x = (-2)**(cnt-1)
    rl = [1]
    for i in range(0, cnt-1)[::-1]:
        if i%2:
            min_x = (-2)**i
            max_x = (-2)**i
            for idx in range(i):
                if idx%2:
                    min_x += (-2)**idx
                else:
                    max_x += 2**idx

            if min_x <= (num - x) <= max_x :
                x -= 2**i
                rl.append(1)
            else:
                rl.append(0)

        else:
            min_x = 2**i
            max_x = 2**i
            for idx in range(i):
                if idx%2:
                    min_x += (-2)**idx
                else:
                    max_x += 2**idx
        
            if min_x <= (num - x) <= max_x:
                x += 2**i
                rl.append(1)
            else:
                rl.append(0)

    print(''.join(str(k) for k in rl))