import os


def middle_ball():
    human = str(input("Введите имя ученика: "))
    surname = str(input("Введите фамилию ученика: "))
    try:
        number1 = int(input("Введите бал по Алгебре: "))
        number2 = int(input("Введите бал по Геометрии: "))
        number3 = int(input("Введите бал по Истории: "))
        number4 = int(input("Введите бал по Укр_мове: "))
        number5 = int(input("Введите бал по Укр_лит: "))
        number6 = int(input("Введите бал по Англ_мова: "))
        number7 = int(input("Введите бал по Химии: "))
        number8 = int(input("Введите бал по Информатики: "))
        list_number1 = [number1, number2, number3, number4, number5, number6, number7, number8]
        twelve = [12]
        sum_of_items = 8
        if list_number1 <= twelve:
            a = sum(list_number1)
            global rating_class
            rating_class = [f"Ученик {human} {surname}, средний бал {a // sum_of_items}"]
            name = 'Рейтинг_Ученика'
            os.makedirs(name)
            os.chdir(f'D:{name}')
            with open(f"{human} {surname}.txt", "w") as file:
                file.write(str(rating_class))
        else:
            print("Вы ввели оценку больше 12")
    except ValueError:
        print("Введите число цыфрами")


try:
    item = int(input("Напишитее сколько учеников у вас в классе: "))

    def class_class():
        for i in range(item):
            middle_ball()
        rating_class.sort()
        print(rating_class)
    class_class()

except ValueError:
    print("Введите число цыфрами")