# 베르트랑 공준

def prime_x(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2)+1)):
        if num % i == 0:
            return False
    return True

list_prime = []

for k in range(2, 246913):
    if prime_x(k):
        list_prime.append(k)

while True:
    n = int(input())
    if n == 0:
        break
    list_x = []
    for i in list_prime:
        if n < i <= 2*n:
            list_x.append(i)
    print(len(list_x))