# Как работать с файлами:
# Связать файловую переменную с файлом
#  a-   открытие для добавления данных
#  r- открытие для чтения файлов
#  w - открытие для записи файлов
# colors = ["red", "green", "blue"] # набор данных
# data = open ("file.txt" , "w") # файловая  переменная a или  r или w ,  связываем ее с тексовым файлом
# data.writelines(colors) # запись набора данных, разделителей не будет
# data.close() # закрыть или разорвать подключение
#_______________________2 _________
# colors = ["red", "green", "blue"] # набор данных
# data = open ("file.txt" , "a") # файловая  переменная a или  r или w ,  связываем ее с тексовым файлом
# data.write("Line 121\n")
# data.write("Line 131\n")
# data.close() # закрыть или разорвать подключение
# _______________3___________
# with open ("file.txt", "a" ) as data:
#   data.write("Line 12111\n")
#   data.write("Line 13111\n")
#_____________________4______________
# path = "file.txt" # чтение файла 
# data = open (path, "r")
# for line in data:
#     print(line) # оператор делает переход на новую строку
# data.close()  
# _________Функции_______

# import lec1 as l
# print (l.f(1))       
# __________ Передача неорганиченного количества аргументов____

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res +=item
#     return res
# print(concatenatio("a", "s","d", "W")  #asdW
# print(concatenatio("a", "1")) # a1
# # print(concatenatio(1,2,3,4))  # TypeError т к используем строки str. а не передаем числа
#__________________2 ___________________
# def concatenatio(*params):
#     res: int = 0 # указание типа не обязательно res=0
#     for item in params:
#         res +=item
#     return res
# print(concatenatio(1,2,3,4))  # 1+2+3+4=10
#________________________________
# a , b= 3 , 4
# (a )= (3 , 4) # кортеж
# print (a)
# print (a [0]) # ожидаем получить 
# print (a [-1]) # ожидаем получить 4

# (a )= (3 , 4, 7, 8) # кортеж
# print (a) # (3, 4, 7, 8)
# print (a [0]) # ожидаем получить 3
# print (a [-1]) # ожидаем получить 8
# exit() # функция не позволяет запускать код ниже
#_________________________________________
#(a )= (3 ,) # кортеж из одного элемента
# print (a)
#___________________перебор кортежей при помощи цикла_________
# (a )= (3 ,4, 5, 7)
# for item in a:
#     print (item)
# типы ключей могу отличаться
# dictionary = {}
# dictionary = \
# {
#     "up": " вверх ",
#     "left": " влево ",
#     "down": " вниз ",
#     "right": " вправо",
# }    
# #for k in dictionary.keys(): # вывод ключей up left down right
# for k in dictionary.values(): # вывод ключей вверх  влево  вниз  вправо
#       print(k)
#_________Множества
# colors = {"red", "green" ,"blue"}
# ## print(type(colors)) # <class 'set'>
# colors.add("gray") # добавили{'green', 'red', 'blue', 'gray'}
# colors.remove("gray") # удалить{'green', 'red', 'blue'}/ tckb elfkbnm если удалить элемет которого нет, то ошибка
# colors.discard("red") # удалить{'green', 'red', 'blue'} ошибки не будет
# colors.clear("") # очистить множество{}

# print(colors) #  {'red', 'green', 'blue'}
#-----------------------------

# a ={1,2,3,4,5,8} #  одно множество
# b ={2,5,8,13,21} # второе множество
# c =a.copy() # c= {1,2,3,4,5,8} # множество на основе имеюшегося
# u = a.union (b) # u = {1,2,3,5,8,13,21} # объединение множеств 
# i = a.intersection (b) # i= {8,2,5}
# dl = a.difference (b) # dl= {1,3}
# dr = b.difference (a) # dr = {13,21}
# q=a\
#     .union(b) \
#     .difference(a.intersection(b))    
#___________Списки
# list1 = [1,2,3,4,5]
# list2  = list1
# list1[0]=123 
# list2[1] =333

# for e in list1:
#     print(e)

# print()    

# for e in list2:
#     print(e)
#_____________удаление последнего элемента списка

# list1 = [1,2,3,4,5]

# print(len(list1))# сколько элементов в лист1
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

#______________________
# list1 = [1,2,3,4,5]
# print(list1.pop(2)) #удаление второго # 3 #[1, 2, 4, 5]
# print(list1)

#_______________вставка элемента на 2 позицию
# list1 = [1,2,3,4,5]
# print(list1.insert(2,11)) # [1, 2, 11, 3, 4, 5]
# print(list1)

#____________добавление в конец
list1 = [1,2,3,4,5]
print(list1.append(11)) # [1, 2, 3, 4, 5, 11]
print(list1)



exit () # код ниже не выполняется

