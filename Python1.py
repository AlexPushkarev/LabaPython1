a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())
if a != 0:
    s = abs(a - (b * c * (d ** 3)) + (((c ** 5) - (a ** 2)) / a) + ((f ** 3) * (a - 213)))
    print(s)
else:
    print('Деление на ноль не возможно')
