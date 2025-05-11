
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
