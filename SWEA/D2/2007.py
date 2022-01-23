# 패턴 마디의 길이

T = int(input())

for i in range(1, T+1):
    word = input()
    list_l = []
    for j in word:
        list_l.append(j)
        if ''.join(list_l) + ''.join(list_l) in word:
            print(f'#{i} {len(list_l)}')
            break
