# 골드바흐의 추측


def prime_x(num):
    if num == 1:
        return False
    for k in range(2, int(num**(1/2)) + 1):
        if num % k == 0:
            return False
    return True

list_prime = []
for k in range(2, 10001):
    if prime_x(k):
        list_prime.append(k)

T = int(input())

for i in range(T):
    n = int(input())
    x = 0
    for j in range(0, len(list_prime)):
        if x == list_prime[j-1]:
            break
        elif list_prime[j] >= n//2:
            for k in range(0, j+1):
                if n == list_prime[j] + list_prime[k]:
                    x, y = list_prime[j], list_prime[k]
                    break
    print(y, x)