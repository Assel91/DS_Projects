"""Напишем игру в которой компьютер сам загадывает число и сам отгадывает"""
import numpy as np

def predict_number(number:int=1)-> int:
    """Функция принимает число, затем считает количество попыток за которое комп угадывает его

    Args:
        int (int, optional): число. Defaults to 1.

    Returns:
        int: количество попыток для поиска
    """
    count = 0 #Создаем переменную для счета количества попыток
    while True:#Запускаем цикл пока не вернется True
        count += 1
        guess_number = np.random.randint(1, 101) #подбираем рандомное число
        if number == guess_number: #устанавливаем условие, если рандомное число равно загадонному останаваливаемся
            break
    return count

def predict_number_v2(number:int=1)-> int:
    """Функция принимает число, затем считает количество попыток за которое комп угадывает его,
    при этом если загадонное число больше рандомного то прибавляет к рандомному +1 и наоборот

    Args:
        int (int, optional): число. Defaults to 1.

    Returns:
        int: количество попыток для поиска
    """
    count = 0
    predicted_number = np.random.randint(1, 101) #Подбираем рандомное число
    
    while number != predicted_number: #Запускаем цикл до возвращения рандомного числа равного загаданному
        count += 1
        if number > predicted_number: #Если загадонное число больше подобранного то прибавляем к подобранному + 1
            predicted_number += 1
        elif number < predicted_number: #Если загадонное число меньше подобранного то минусуем -1
            predicted_number -= 1
    return count

def predict_number_v3(number:int=1)-> int:
    """Функция принимает число, затем считает количество попыток за которое комп угадывает его.
    Поиск производится через бинарный поиск. 
    Составляется список из 100 чисел от 1 до 100, если загадонное число лежит в диапазоне от середины до
    100, то поиск сужается от середины списка до максимального значения списка. Далее полученный список сужается
    еще по полам и так далее, пока рандомное число не будет равно загадонному

    Args:
        int (int, optional): число. Defaults to 1.

    Returns:
        int: количество попыток для поиска
    """
    count = 0
    search_list = list(range(1,101)) #Согласно задаче загадонное число может быть в диапазоне от 1 до 100
    low = 0 
    high = len(search_list)-1
    
    while low <= high:
        count += 1
        midd = (low+high)// 2 #Находим индекс серединного числа списка
        guess_number_to_search = search_list[midd] #Находим значение серединного числа в списке
        
        if number == guess_number_to_search:
            break
        elif number < guess_number_to_search:
            high = midd -1
        else:
            low = midd + 1
    return count

# print(f"Количество попыток {predict_number(99)}")

def score_game(predict_number)-> int:
    """ За какое количество попыток, в среднем на 1000 попыток алгоритм угадывает число

    Args:
        predict_number (_type_): функция подсчета количества попыток
    Returns:
        int: количество попыток
    """
    count_ls = [] #Список для сохранения попыток
    np.random.seed(1) #Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = 1000) #Создаем список из 1000 случайных чисел 
    
    for number in random_array:
        count_ls.append(predict_number(number))
    
    score_mean = np.mean(count_ls)
    score_median = round(np.median(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за {score_median} попыток')
    # return score_median

if __name__ == '__main__':
    score_game(predict_number)