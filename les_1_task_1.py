n = int(input("Введите трехзначное число: "))

a1 = n % 10
a2 = n % 100 // 10
a3 = n // 100

print(f"Сумма цифр числа:{a1 + a2 + a3}, \nПроизведение цифр числа:{a1 * a2 * a3}")
