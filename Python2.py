import random

count = 1
while count != 0:
    print('Угадайте число')
    a = random.randint(1, 10)
    c = int(input())
    if c == a:
        print('Вы угадали число')
    else:
        print('Вы не угадали число')
    print('Повторить? Нажмите 1')
    print('Иначе 0')
    count = int(input())
