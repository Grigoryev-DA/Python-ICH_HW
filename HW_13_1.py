# 1. Напишите программу, которая принимает два числа и возвращает их сумму
# и произведение в виде кортежа (sum, product). Используйте функцию для
# вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print.

def sum_product(a,b):
    result = ((a + b), (a * b))
    print(f"Сумма и произведение чисел: {result}")

sum_product(10, 10)

