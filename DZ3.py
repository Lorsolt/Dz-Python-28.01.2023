"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""

n = int(input("Введите число - "))

summa = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

print("Сумма чисел n + nn + nnn - %d" % summa)
