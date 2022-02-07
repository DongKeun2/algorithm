# ROT13

word = input()

result = []
for s in word:
    if s.islower():
        if ord(s)+13 > 122:
            result.append(chr(ord(s)+13-26))
        else:
            result.append(chr(ord(s)+13))

    elif s.isupper():
        if ord(s)+13 > 90:
            result.append(chr(ord(s)+13-26))
        else:
            result.append(chr(ord(s)+13))
    else:
        result.append(s)

print(''.join(result))
