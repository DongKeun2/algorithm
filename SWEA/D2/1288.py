# 새로운 불면증 치료법

T = int(input())

for i in range(1, T+1):
    n = int(input())

    cnt = 0
    idx= 1
    n_set = set()

    while len(n_set) < 10:
        n = n*idx

        x = str(n)
        for k in x:
            n_set.add(k)
        
        n = n//idx
        idx += 1
        cnt += 1
    
    print(f'#{i} {n*cnt}')
