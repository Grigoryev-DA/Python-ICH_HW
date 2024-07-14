"""2. Напишите программу, которая принимает список чисел от пользователя
и сортирует его в порядке убывания, используя метод sort() и параметр reverse=True.
Выведите отсортированный список на экран.
"""

# функция формирует список чисел из введенной строки
def list_generation():
    list = input("Введите числа для сортировки через пробел: ").split()
    number_list = []
    for i in list:
        number_list.append(int(i))
    return number_list


# функция сортирует список в порядке убывания
def list_sorting(list):
    number_list = list
    number_list.sort(reverse=True)
    print(number_list)

list_sorting(list_generation())
