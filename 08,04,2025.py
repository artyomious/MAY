

#4 Задача
result = [i for i in range (1,101) if i % 3== 0 and i % 5 ==0]

print ( result)


#1 Задача
a= int(input('Введите а ='))
b= int(input('Введите b ='))

result = [i**2 for i in range (a,b+1)]
print ( result)

#2 Задача

a= int(input('Введите а ='))
b= int(input('Введите b ='))

result = [i for i in range (a,b+1) if i % 2== 0]
print ( result)

#3 Задача

array= input('Введите строку')
result = [i for i in array.lower() if i in 'аеёиоуыэюяaqeyoiuj']
print ( result)


#5 Задача

n=3
result = [[i+1+j*n for i in range (n)] for j in range (n)]

print ( result)



#2 Задача
day = input("Введите день недели (на английском): ")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} — рабочий день")
    case "Saturday" | "Sunday":
        print(f"{day} — выходной день")
    case _:
        print("Ошибка: введите корректное название дня недели")

#1 Задача
bkv = input("Введите букву (на английском): ").lower()

match bkv:
    case "a" | "y" | "o" | "e" | "u"| "i":
        print(f"{bkv} — Гласная")

    case _:
        print(f"{bkv} — Согласная")



#3 Задача
fruit = input("Введите название фрукта: ").lower()

match fruit:
    case "cherry":
        print(f"{fruit} — красный")
    case "banana" | "lemon":
        print(f"{fruit} — жёлтый")
    case "orange" :
        print(f"{fruit} — оранжевый")
    case "plum":
        print(f"{fruit} — фиолетовый")
    case _:
        print(f"Неизвестный цвет для фрукта {fruit}")



# 4 Задача
a = input("Введите оценку (1-5): ")

match a:
    case "5":
        print("Отлично!")
    case "4":
        print("Хорошо")
    case "3":
        print("Удовлетворительно")
    case "2":
        print("Неудовлетворительно")
    case "1":
        print("Плохо")
    case _:
        print("Ошибка: оценка должна быть от 1 до 5")