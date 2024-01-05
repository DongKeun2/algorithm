# Hashing / 브론즈2
L = int(input())
word = input()
print(sum((ord(word[i]) - 96) * 31 ** i for i in range(L)) % 1234567891)