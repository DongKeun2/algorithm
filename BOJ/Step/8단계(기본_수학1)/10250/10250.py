# ACM 호텔

T = int(input())

for i in range(T):
    H, W, N = list(map(int, input().split()))
    if N <= H:
        print(f'{N}01')

    else:
        room_1 = H
        room_2 = 1
        while N > room_1:
            room_1 += H
            room_2 += 1
        print((H-(room_1 - N))*100 + room_2)