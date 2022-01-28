# 숫자를 정렬하자

T = int(input())

for i in range(1, T+1):
    
    N = int(input())

    num = [ n for n in list(map(int, input().split()))]
    num.sort()
    result = ' '.join(str(x) for x in num)
    print(f'#{i} {result}') 
