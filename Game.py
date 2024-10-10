"""Игра для поиска случайных чисел"""

import numpy as np
number = np.random.randint(1, 101)

count = 0
while True:
    count += 1
    predict_number = int(input("Угадайте число от 1 до 101"))
    if predict_number > number:
        print("Число должно быть меньше")
    elif predict_number < number:
        print("Число должно быть больше")
    else:
        print(f"Вы угадали число: {number}, за {count} количество попыток")
        break 
