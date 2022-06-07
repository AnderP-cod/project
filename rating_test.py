def middle_ball():
    human = str(input("Введите свое имя: "))
    number1 = int(input("Введите бал по Алгебре: "))
    if number1 <= 12:
        number2 = int(input("Введите бал по Геометрии: "))
        if number2 <= 12:
            number3 = int(input("Введите бал по Истории: "))
            if number3 <= 12:
                number4 = int(input("Введите бал по Укр_мове: "))
                if number4 <= 12:
                    number5 = int(input("Введите бал по Укр_лит: "))
                    if number5 <= 12:
                        number6 = int(input("Введите бал по Англ_мова: "))
                        if number6 <= 12:
                            number7 = int(input("Введите бал по Химии: "))
                            if number7 <= 12:
                                number8 = int(input("Введите бал по Информатики: "))
                                if number8 <= 12:
                                    a = number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8
                                    print(f"Ученик {human}, средний бал {a // 8}")
                            else:
                                print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
                        else:
                            print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
                    else:
                        print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
                else:
                    print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
            else:
                print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
        else:
            print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")
    else:
        print("Ошибка_1 :Вы ввели бал не буквами или вы ввели бал больше 12")


try:
    item = int(input("Напишитее сколько учеников у вас в классе: "))
    for i in range(item):
        g = [middle_ball()]
        g.sort(reverse=True)
        print(g)


except ValueError:
    print("Введите число цыфрами")



