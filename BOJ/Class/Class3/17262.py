# Four Squares, 실버3
# pypy3 통과

n = int(input())
answer = 5

lst = [5] * (n+1)
for x in range(1, int(n**(1/2))+1):
    lst[x**2] = 1
for i in range(1, n+1):
    for j in range(1, int(n**(1/2))+1):
        if i <= j**2: break
        lst[i] = min(lst[i], lst[i-j**2] + 1)
print(lst[n])

# def solution(N):
#     if (N**.5).is_integer(): return 1

#     set_1 = {i**2 for i in range(int(N**.5),0,-1)} # N 이하 제곱수들
#     for i in set_1:
#         if N-i in set_1: return 2
    
#     while N%4==0:
#         N //= 4    
#     return 4 if N%8==7 else 3

# print(solution(int(input())))