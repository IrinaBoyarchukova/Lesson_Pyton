print ("hello world")
# типы данных и переменная
# int , float , boolean, str, list, None
#value = None
#a=123
#b=1.23
#print(a)
#print(b)
#value=1234
#print (value)
#print (type (a))
#s=" hello \n world" # строковая переменная (\n перенос)
#print (s)
#print(a,b,s)
#f= False # описание логической части
#print (f)
#list = [1,2, "hello" ]
#print (list)
# ввод и вывод данных
# print, input
#print ("Введите a")
#a = int(input ())
#print ("Введите b")
#b= int(input ())
#print(a,"+", b, "=", a+b)
#(f"{a} {b}")
# арифмитические операции +,-,*,/,**
# **,//, %
# (), Сокращенные операции
#a=2
#b=8
#c=a**b # возведение в степень
#print(c)
#a=1.88888
#b=3
#c= round (a*b,5) # округление по 5
#print(c) # htpekmnfnn 3.900000004 ' особенность пайтон
#a=3
#a+=5
#print(a)
# Логические операции

#a=1>3 and 5>2
#print(a)
# Управляющие конструкции
# if, if-else, while, else

#a=int(input("a="))
#b=int(input("b="))
#if a>b:
#    print(a)
#else:
#    print(b)
#
#username=input("Введите имя:")
#if username =="Маша":
#    print("Ура,это же Маша!")
#elif username =="Марина":
#    print ("Я так ждала Вас, Марина!")
#elif username == "ильнар":
#   print("Ильнар-топ")
#else:
#    print("Привет,", username)

#original=23
#inverted=0
#while original !=0:
#    inverted = inverted*10 + (original%10)
#    original//=10
#else:
#   print("Пожалуй")
#    print("хватит)")    
#print( inverted )
# Управляющие констркции:
#for
#for i in 1,2,3,4,5:
#    print(i**2) # квадрат чисел
#list = [1,2,3,4,10,5]
#for i in list:
#    print(i)
# Использование range
#r=range(10) # Получаем значение от 0 до 9
#for i in range(10):
#    print(i)
#for i in range(1,5):
#    print(i)
#for i in range(1,5,2): # вывод нечетных чисел в диапазоне
#    print(i)
#for i in "qwert": # побуквенная разбивка
#    print(i)
#text = " съешь меня "
#print(text)
#print(len(text))
#help(int)

# Функции
def f(x):
    if x==1:
        return "Целое" # строка str 
    elif x==2.3:
        return 23      # число int
    else:
        return
# arg=2.3
# print(f(arg))  
# print(type(f(arg)))      
