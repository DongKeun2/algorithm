# 크로아티아 알파벳

word = input()

alp_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alp_list:
    word = word.replace(i, '1')

num = len(word)
print(num)