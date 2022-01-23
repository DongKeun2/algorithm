# 몫과 나머지 출력하기

T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split())) 
    print(f'#{i} {A//B} {A%B}')