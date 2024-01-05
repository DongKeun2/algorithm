# 팰린드롬수 / 브론즈1

while True:
    n = str(input())
    if n == '0': break

    answer = 'yes'
    for i in range(len(n)//2):
        if not n[i] == n[-(i+1)]: answer = 'no'
    print(answer)