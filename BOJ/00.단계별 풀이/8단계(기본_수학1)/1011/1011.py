T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
	
    dist = y - x

    if dist == 1:
        print(1)
    else:
        cnt = 1
        cnt_t = 1
        result = 1
        total = 2
        while dist >= total:
            total += cnt
            cnt_t += cnt
            if cnt_t == cnt * 2 :
                cnt += 1
                cnt_t = 0
            result += 1

        print(result)