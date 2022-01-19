S = input()

a_to_z = list(range(97,123))

for i in a_to_z:
    print(S.find(chr(i)))