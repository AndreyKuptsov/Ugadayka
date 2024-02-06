
import random
user_name = input('Hello! Enter you name: ')
num = random.randint(1, 101)
user_num = float(input('Enter number '))
while user_num != num:
        print(f'Oops, {user_name}, try again')
        user_num = float(input('Enter number '))
else:
    print(f'Yes! {user_name}, you are Wonderful!')
