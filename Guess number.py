import random

import time    # импортируем функцию для подсчета времени выполнения программы 

from choose_plural import choose_plural

MINN = 1
MAXN = 10 ** 4300    # максимум, что позволяет Питон

num = random.randint(MINN, MAXN - 1) 

n = MINN
m = MAXN
   
time0 = time.time_ns()    # устанавливаем старт времени


guess = (n + m) // 2

print(guess)

count = 1

while num != guess:
    if num > guess:
        print("Больше!")
        n = guess
    else:
        print('Меньше!')
        m = guess
    guess = (n + m) // 2
    print(guess)
    count += 1    

time1 = time.time_ns()     # устанавливаем стоп времени

print("Угадал!!!")
print(f"Использовал {count} {choose_plural(count, ['попытка', 'попытки', 'попыток'])}.") 

print(f"Затрачено {time1 - time0} {choose_plural(time1 - time0, ['наносекутда', 'наносекунды', 'наносекунд'])}.")    # производим подсчет затраченного времени в наносекундах


# time0 = time.time_ns()    # устанавливаем старт времени

# n = 189
# print(pow(189, 234))

# time1 = time.time_ns()     # устанавливаем стоп времени


# print(time1 - time0,"ns")    # производим подсчет затраченного времени в наносекундах