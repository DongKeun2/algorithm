# 무한 사전

T = int(input())

for i in range(1, T+1):
    p = input().rstrip()
    q = input().rstrip()

    if p + 'a' == q:
        print(f'#{i} N')
    else:
        print(f'#{i} Y')

