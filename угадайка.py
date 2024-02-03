
import random
user_name = input('Привет! Как тебя зовут? ')
num = random.randint(1, 101)
user_num = float(input('Введите число: '))
while True:
    if user_num != num:
        print(f'Не угадал, {user_name}, попробуй еще раз')
        user_num = float(input('Введите число: '))
else:
    print(f'Ура! {user_name}, это именно то число!')