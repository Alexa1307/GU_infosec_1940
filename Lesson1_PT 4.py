# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# Вариант1
n = int(input("Введите целое положительное число "))
x = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > x:
        x = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", x)
        break

# Вариант 2
n = int(input("Введите целое положительное число "))
x = 1 # переменная необходима для работы в цикле.
while n >= 1:
    d = n % 10
    n = n // 10
    if d > x:
        x = d
print("Максимальное цифра в числе ", x)