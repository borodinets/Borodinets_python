
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
def num(x1,y1,x2,y2): 

    print(f'длина отрезка = ' "%.2f" %((x2-x1)**2+(y2-y1)**2)**(0.5))
     
num (float(input('введите x1: ')),
float(input('введите y1: ')),
float(input('введите x2: ')),
float(input('введите y2: ')))