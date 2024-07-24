# 다이얼

dial = input()

time = 0
for i in dial:
    if 65 <= ord(i) <= 67:
        time += 3
    elif 68 <= ord(i) <= 70:
        time += 4
    elif 71 <= ord(i) <= 73:
        time += 5
    elif 74 <= ord(i) <= 76:
        time += 6
    elif 77 <= ord(i) <= 79:
        time += 7
    elif 80 <= ord(i) <= 83:
        time += 8
    elif 84 <= ord(i) <= 86:
        time += 9
    elif 87 <= ord(i) <= 90:
        time += 10
print(time)