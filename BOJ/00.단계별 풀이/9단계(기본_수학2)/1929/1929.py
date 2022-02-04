# 소수 구하기

M, N = map(int, input().split())

def pirme_num(i):
    if i == 1:
        return False
    else:
        for k in range(2, int(i ** (1/2))+1):
            if i % k == 0:
                return False
        return True


for i in range(M, N+1):
    if pirme_num(i):
        print(i)