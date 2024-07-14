# 2. Напишите программу, которая принимает список чисел и возвращает сумму,
# минимальное и максимальное значение из списка. Используйте функцию для
# обработки списка чисел и возврата трех значений.
# Выведите результат на экран с помощью команды print.


# функция возвращает три отдельных значения
def calculations(list):
    sum = my_sum(list)
    max, min = my_max_min(list)
    print("Сумма чисел: ", sum)
    print("Минимальное значение: ", min)
    print("Максимальное значение: ", max)

# функция сложения
def my_sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

# функция поиска минимума и максимума
def my_max_min(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min

list = [3, 7, 2, 9, 1, 5]

calculations(list)