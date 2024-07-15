# FizzBuzz, 브론즈1

a = input()
b = input()
c = input()

if a.isdecimal(): a, target = int(a), 'a'
if b.isdecimal(): b, target = int(b), 'b'
if c.isdecimal(): c, target = int(c), 'c'

if target == 'a':
    tmp = (a+1 if (a+1)%5 else 'Buzz') if (a+1) % 3 else ('Fizz' if (a+1)%5 else 'FizzBuzz')
    answer = int(a) + 3  if tmp == b else int(a) - 3
elif target == 'b':
    tmp = (b+1 if (b+1)%5 else 'Buzz') if (b+1) % 3 else ('Fizz' if (b+1)%5 else 'FizzBuzz')
    answer = int(b) + 2  if tmp == c else int(b) - 2
else:
    tmp = (c-1 if (c-1)%5 else 'Buzz') if (c-1) % 3 else ('Fizz' if (c-1)%5 else 'FizzBuzz')
    answer = int(c) + 1  if tmp == b else int(c) - 1
print((answer if answer%5 else 'Buzz') if answer % 3 else ('Fizz' if answer%5 else 'FizzBuzz'))