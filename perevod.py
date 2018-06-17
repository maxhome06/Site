# перевод из десятичной в двоичную
def dec_to_bin(x):
    n = ""
    print(x)
    if x.isdigit() == False:
        print("Вы ввели не число")
    else:
        b = int(x)
        while b > 0:
            y = str(b % 2)
            n = y + n
            b = int(b / 2)
        print(n)

# перевод из двоичной в десятичную
def bin_to_dec(x):
    str = "01"
    if x[0] not in str:
        print ("Введены недопустимые символы")
    else:
        dlina = len(x)
        otvet = 0
        for i in range(0, dlina):
            otvet = otvet + int(x[i]) * (2 ** (dlina - i - 1))
        print(otvet)

while True:
    print("Программа перевода чисел")
    print("[1]: Перевод из десятичной системы в двоичную")
    print("[2]: Перевод из двоичной в десятичную")
    print("[3]: Выход из программы")
    c = int(input("Выберите действие:"))
    if c == 1:
        x = input("Введите число:")
        dec_to_bin(x)
    elif c == 2:
        x = input("Введите число:")
        bin_to_dec(x)
    elif c == 3:
        break
    else:
        print("Вы ввели неправильную команду")
        continue
