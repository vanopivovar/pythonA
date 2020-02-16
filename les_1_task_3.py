# https://drive.google.com/file/d/12ERjfIkv_Koc7r_4d6y30mAzpkBg_aDy/view?usp=sharing
# Начало
# Ввод координат x1, y1, x2, y2
# Вычисляем угловой коэффициент k
# Вычисляем b
# Проверяем условие, если b < 0, в уравнении b вписываем в скобки, если b > 0 изменений нет
# Вывод резульатов вычисления
# Конец

x1 = int(input("Введите кородинату x1 "))
y1 = int(input("Введите кородинату y1 "))
x2 = int(input("Введите кородинату x2 "))
y2 = int(input("Введите кородинату y2 "))

k = int(((y2 - y1) / (x2 - x1)))
b = y2 - (k * x2)
if b < 0:
    print(f"y = {k}x + ({b}) ")
else:
    print(f"y = {k}x + {b} ")
