# Base64 Decoder

T = int(input())

for i in range(1, T+1):
    words = input()

    word_num = []
    for word in words:
        if 65 <= ord(word) <= 90:
            word_num.append(ord(word) - 65)
        elif 97 <= ord(word) <= 122:
            word_num.append(ord(word) - 71)
        else:
            word_num.append(ord(word) +4)

    list_2 = [32, 16, 8, 4, 2, 1]
    word_2 = []
    for word in word_num:
        x = word
        for l_2 in list_2:
            if x >= l_2:
                x -= l_2
                word_2.append(1)
            else:
                word_2.append(0)
    
    list_num = []
    for k in range(len(word_2)//8):
        list_num.append(word_2[k*8:k*8+8])

    list_3 = [128, 64, 32, 16, 8, 4, 2, 1]

    r_num = []
    for num in list_num:
        n = 0
        for idx in range(len(num)):
            if num[idx] == 1:
                n += list_3[idx]
        r_num.append(n)

    result = []
    for r in r_num:
        result.append(chr(r))

    print(f'#{i}', ''.join(result))




