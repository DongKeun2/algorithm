# 반반

T = int(input())

for i in range(1, T+1):
    s = input()
    for w in s:
        if  s.count(w) != 2:
            print(f'#{i} No')
            break
    else:
        print(f'#{i} Yes')