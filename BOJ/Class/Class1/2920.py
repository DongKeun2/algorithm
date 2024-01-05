# 음계 / 브론즈 2

str = ''.join(map(str, input().split()))
answer = 'mixed'
if str == '12345678':
    answer = 'ascending'
elif str == '87654321':
    answer = 'descending'
print(answer)