# 문자열 반복

T = int(input())
for i in range(T):
    R, word = input().split()
    print_word = []
    for k in word:
        print_word.append(k*int(R))
    print(''.join(print_word))