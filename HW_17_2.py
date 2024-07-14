"""2. Напишите программу, которая принимает произвольное количество аргументов
от пользователя и передает их в функцию calculate_sum, которая возвращает сумму всех аргументов.
Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран."""

# функция формирует список значений
def list_generation():
    list = input("Введите числа через пробел: ").split()
    number_list = []
    for i in list:
        number_list.append(int(i))
    return number_list


digital_list = (list_generation())

# функция принимает неограниченный список аргументов и сумирует их
def calculate_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(calculate_sum(*digital_list))

