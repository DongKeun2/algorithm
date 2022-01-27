# 초심자의 회문 검사

T = int(input())

for i in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')