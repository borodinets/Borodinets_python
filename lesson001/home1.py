# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
a = int(input('введите число : '))
if a < 1 or a > 7:
    print("error")

elif a < 6:
        print("нет")
        
else:
       print("да")
    