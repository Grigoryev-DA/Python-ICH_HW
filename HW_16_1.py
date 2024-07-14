"""1. Напишите программу, которая принимает матрицу (вложенный список)
от пользователя и находит сумму всех элементов в матрице.
Используйте вложенные списки и циклы для обхода элементов матрицы."""

# функция создает и заполняет матрицу
def matrix():
    size = int(input("Введите размер матрицы: "))
    matr = []
    for i in range(size):
        string = []
        for i in range(size):
            string.append(int(input("Введите число: ")))
        matr.append(string)
    return matr




matrix = matrix()
# функция прохлжит по каждому элементу всех вложенных списков, и сумирует все елементы списков
def sum_elements_matrix(matrix):
    sum = 0
    for list in matrix:
        for number in list:
            sum += number
    return sum


print(sum_elements_matrix(matrix))