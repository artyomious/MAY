# 1 ЗАДАЧА

s = input("Введите строку: ")
vowels = "аеёиоуыэюяaeiouy"
count = 0
for a in s.lower():
    if a in vowels:
        count += 1
print("Количество гласных букв:", count)


s = input("Введите строку: ")
vowels = "аеёиоуыэюяaeiouy"
count = 0
i = 0
while i < len(s):
    if s[i].lower() in vowels:
        count += 1
    i += 1
print("Количество гласных букв:", count)

# 2 ЗАДАЧА

s = input("Введите строку: ")
words = s.split()
count = 0
for word in words:
    if 'a' in word.lower():
        count += 1
print("Количество слов с буквой 'a':", count)

# 3 ЗАДАЧА

a = int(input("Первое число: "))
b = int(input("Второе число: "))

n = max(a, b)
while True:
    if n % a == 0 and n % b == 0:
        print("НОК:", n)
        break
    n += 1


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

n = max(a, b)

for c in range(n, a * b + 1):
    if c % a == 0 and c % b == 0:
        print(f"НOK :")
        break
else:
    print(f"Не удалось найти НОК для чисел ")