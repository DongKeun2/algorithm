# 백만 장자 프로젝트

T = int(input())

for k in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    total = 0
    max_price = price[0]
    idx = 0
    for i in range(len(price)):
        if max_price <= price[i]:
            max_price = price[i]
            idx = i
    if idx != 0:
        for i in range(0, idx):
            total += price[idx] -price[i]
    while True:
        if idx == len(price) -1:
            break
        idl = idx + 1
        if idl == len(price) -1:
            break
        max_price = 0
        for i in range(idl, len(price)):
            if max_price <= price[i]:
                max_price = price[i]
                idx = i
        if idx != idl:
            for i in range(idl, idx):
                total += price[idx] - price[i]
    print(f'#{k} {total}')
