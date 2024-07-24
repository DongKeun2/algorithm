# 피보나치 수 5

def my_Fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return my_Fibonacci(num - 2) + my_Fibonacci(num - 1)


n = int(input())
print(my_Fibonacci(n))