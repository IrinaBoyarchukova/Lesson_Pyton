# def f(x):
#     x ** 2
# g=f
# #print(type(f)) # <class 'function'>
# print (f(1)) #None
# print (g(1)) # None
#_____________2_________
# def f(x):
#     return x**2
# g=f # приравниваем функции
# print (type(f))
# print (type(g)) 

# print (f(4)) 
# print (g(4)) 

#______________3_________
# def calc (x):
#     return x+10
# print(calc(10)) # 20

#______________4_________
# def calc1 (x):
#     return x+10
# print(calc1(10))   #20 калькулятор 10+10

# def calc2 (x):
#     return x+10
# print(calc2(10))   #20
# ______________5_______________
# def calc1 (x):
#     return x+10

# def calc2 (x):
#     return x*10

# def math (op, x):
#     print(op(x))
# math (calc2, 10)    
# math (calc1, 10) 
#______________6 функция с двумя переменными_________________
# def sum (x,y):
#     return x+y # функция сложения

# f=sum
# def mylt (x,y):
#     return x * y

# def calc (op, a, b): # функция в качестве аргумента принимает операцию , а качестве орепанды два аргумента    print(op(x))
#     print(op (a, b))
#     #return op (a,b)
    
# calc (f, 4, 5)
#_____________7_________
# \\\def sum (x,y):
#  \\\   return x+y # функция сложения

# sum =lambda x,y:x+y

# def mylt (x,y):
#     return x * y

# def calc (op, a, b): # функция в качестве аргумента принимает операцию , а качестве орепанды два аргумента    print(op(x))
#     print(op (a, b))
#     #return op (a,b)
    
# calc (sum, 4, 5)
#____________8_________

# sum 

# def mylt (x,y):
#     return x * y

# def calc (op, a, b): # функция в качестве аргумента принимает операцию , а качестве орепанды два аргумента    print(op(x))
#     print(op (a, b))
#     #return op (a,b)
    
# calc (lambda x,y:x+y, 4, 5)
# _________использование Lambd_________
#  Создаем список в диопазоне от 1 до 100

# list = []

# for i in range(1,101):
#     if(i%2 == 0): # остаток от деления = 0
#         list.append(i)
# print(list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
# # 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
# _________использование Lambd_________
#  Создаем список в диопазоне от 1 до 100

# list = []

# for i in range(1,101):
#     if(i%2 == 0): # остаток от деления = 0
#         list.append(i)
# print(list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
# # 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
#_________использование Lambd 2_________
# Создаем список в диопазоне от 1 до 100

# list = []

# for i in range(1,101):
#     # if(i%2 == 0): # остаток от деления = 0
#         list.append(i)
# print(list) 
#_____________________________________________
# list = [i for i in range (1,21) if(i%2 == 0)]
# print(list)#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#_________создать пару чисел, подключаем кортежи______
# list = [(i, i) for i in range (1,21) if(i%2 == 0)]
# print(list) # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

#_________функция________

# def f(x):
#     return x**3 # возведение в степень
# list = [f(i) for i in range (1,21) if(i%2 == 0)]
# #2#list = [(i,f(i)) for i in range (1,21) if(i%2 == 0)]
# print(list) #1 вариант[8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]
# # 2 вариант [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]




#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)


# Функция map
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
# 26, 27, 28, 29]


# функция мэп со считыванием
# data = list(map(int, input().split()))
# print(data)
###in 1 2 3 45
####out [1, 2, 3, 45]


## Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2 , data))
# print(res)

#______________________________________
# c использованием лямбды 2 вариант
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция zip
# user =["user1","user2","user3" ]
# ids =[4,5,9,14,7]
# data = list(zip(user,ids)) 
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9)]

# Функция enumerate
# user =["user1","user2","user3" ]
# ids =[4,5,9,14,7]
# data = list(enumerate(user)) 
# print(data) 
# # [('user1', 4), ('user2', 5), ('user3', 9)]
# [(0, 'user1'), (1, 'user2'), (2, 'user3')]

