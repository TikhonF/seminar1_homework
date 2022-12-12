# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным. Дополнительно: можете проверить, что это действительно число,
# и что это действительно входит в нужный диапазон
# *Пример:* 6 -> да; 7 -> да; 1 -> нет

# day_of_the_week = input('Введите цифру, обозначающую день недели:\n')

# if day_of_the_week.isdigit():
#     digit = int(day_of_the_week)
#     if digit > 7 or digit < 1:
#         print('Это не цифра, обозначающая день недели')
#     elif digit > 5:
#         print('да - этот день выходной')
#     else:
#         print('нет - этот день не является выходным')
# else:
#     print('это не цифра, обозначающая день недели')
    
    
# # 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# # значений предикат. Нужно написать таблицу истинности.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not(x or y or z) == (not x and not y and not z):
#                 #print(f'{x}\t{y}\t{z}\t{":утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат"}')
#                 print(f'{x}\t{y}\t{z}\t{not(x or y or z) == (not x and not y and not z)}')
   
   
                
# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: x=34; y=-30 -> 4; x=2; y=4-> 1; x=-34; y=-30 -> 3;

# x_coordinate = int(input('введите координату x:\n'))
# y_coordinate = int(input('введите координату y:\n'))

# if x_coordinate > 0 and y_coordinate > 0:
#     print('1 - 1-я четверть плоскости координат')
# elif x_coordinate < 0 and y_coordinate > 0:
#     print('2 - 2-я четверть плоскости координат')  
# elif x_coordinate < 0 and y_coordinate < 0:
#     print('3 - 3-я четверть плоскости координат')   
# elif x_coordinate > 0 and y_coordinate < 0:
#     print('4 - 4-я четверть плоскости координат')
# elif x_coordinate == 0 and y_coordinate == 0:
#     print('точка является началом координат') 
# elif x_coordinate == 0:
#     print('точка координат находится на оси ординат')  
# elif y_coordinate == 0:
#     print('точка координат находится на оси абсцисс')



# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).
# Пример: quarter = 1 = x∈(0, ∞) u y∈(0,∞)

# quarter_number = int(input('введите номер четверти плоскости координат от 1 до 4:\n'))
# if quarter_number not in range(1,5):
#     print('вы ввели неверное число')
# elif quarter_number == 1:
#     print('x∈(0, ∞) u y∈(0,∞)')
# elif quarter_number == 2:
#     print('x∈(-∞, 0) u y∈(0,∞)')
# elif quarter_number == 3:
#     print('x∈(-∞, 0) u y∈(-∞, 0)')
# else:
#     print('x∈(0, ∞) u y∈(-∞, 0)')


# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.
# Пример: A (3,6); B (2,1) -> 5.09; A (7,-5); B (1,-1) -> 7.21

print('Введите через пробел координаты первой точки A: ')
x_coordinate1, y_coordinate1 = map(int, input().split(' '))

print('Введите через пробел координаты второй точки B: ')
x_coordinate2, y_coordinate2 = map(int, input().split(' '))

distance = float(((x_coordinate2 - x_coordinate1)**2 + (y_coordinate2 - y_coordinate1)**2)**0.5)
print(int(distance * 100)/100)


     
       
              
                    
        
    
                
               
               



            


                