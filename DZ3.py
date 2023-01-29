"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""
print("Введите число - ")

n = int(input())

summa = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

print("Сумма чисел n + nn + nnn - %d" % summa)
