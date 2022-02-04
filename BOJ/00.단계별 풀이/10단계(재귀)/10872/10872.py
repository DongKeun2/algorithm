# 팩토리얼

def my_factorial(num):
    if num == 0:
        return 1
    return num * my_factorial(num-1)

N = int(input())

print(my_factorial(N))