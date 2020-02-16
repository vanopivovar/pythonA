# https://drive.google.com/file/d/1Z1G5SnQffbbGe1H_LmSDs0E9OXKBOimH/view?usp=sharing
# Начало
# Присвоение значений задачи переменным
# Вычисляем побитовое И
# Вычисляем побитовое ИЛИ
# Вычисляем побитовое Исключающее
# Вычисляем побитовое Отрицание
# Вычисляем побитовый сдвиг влево
# Вычисляем побитовый сдвиг вправо
# Вывод ("Сумма цифр числа:aS Произведение цифр числа:aM")
# Конец

a = 5
b = 6
r1 = a & b
r2 = a | b
r3 = a ^ b
r4 = ~ a
r5 = ~ b
rLeft = a << 2
rRight = a >> 2

print(
    f"Результат И:{r1} "
    f"\nРезультат ИЛИ:{r2}"
    f"\nРезультат Исключения:{r3}"
    f"\nРезультат Отрицания числа 5:{r4}"
    f"\nРезультат Отрицания числа 6:{r5}"
    f"\nРезультат побитовый сдвиг влево:{rLeft}"
    f"\nРезультат побитовый сдвиг вправо:{rRight}"
)
