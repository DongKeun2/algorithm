# 영화감독 숌

N = int(input())

cnt = 0
num = 665
while True:
    if cnt == N:
        print(num)
        break
    num += 1
    if '666' in str(num):
        cnt += 1