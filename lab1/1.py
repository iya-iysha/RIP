from math import sqrt
import sys
    
print('ИУ5-53Б Ваксина Ия Романовна "Решение биквадратного уравнения"\n')
key = 0
keya = 0
keyb = 0
keyc = 0

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
        
except:
    print('С коэффициентами что-то не так. Попробуйте исправить...')

    while key == 0:
         try:
            if len(sys.argv) == 1:
                while keya == 0:
                  a = float(input('Коэффициент А: '))
                  keya = 1
                while keyb == 0:
                  b = float(input('Коэффициент B: '))
                  keyb = 1
                while keyc == 0:
                  c = float(input('Коэффициент C: '))
                  keyc = 1
                key = 1
            
            if len(sys.argv) == 2:
              while keya == 0:
                  if sys.argv[1].isdigit():
                      a = float(sys.argv[1])
                  else:
                      a = float(input('Коэффициент А: '))
                  keya = 1
              while keyb == 0:
                  b = float(input('Коэффициент B: '))
                  keyb = 1
              while keyc == 0:
                  c = float(input('Коэффициент C: '))
                  keyc = 1
              key = 1
            
            if len(sys.argv) == 3:
              while keya == 0:
                if sys.argv[1].isdigit():
                    a = float(sys.argv[1])
                else:
                    a = float(input('Коэффициент А: '))
                keya = 1
              while keyb == 0:
                if sys.argv[2].isdigit():
                    b = float(sys.argv[2])
                else:
                    b = float(input('Коэффициент B: '))
                keyb = 1
              while keyc == 0:
                c = float(input('Коэффициент C: '))
                keyc = 1
              key = 1


            if len(sys.argv) == 4:
              while keya == 0:
                if sys.argv[1].isdigit():
                    a = float(sys.argv[1])
                else:
                    a = float(input('Коэффициент А: '))
                keya = 1
              while keyb == 0:
                if sys.argv[2].isdigit():
                    b = float(sys.argv[2])
                else:
                    b = float(input('Коэффициент B: '))
                keyb = 1
              while keyс == 0:
                if sys.argv[3].isdigit():
                    с = float(sys.argv[3])
                else:
                    с = float(input('Коэффициент С: '))
                keyс = 1
              key = 1

         except:
            print("Некорректный ввод коэффициента! Попробуйте еще раз...\n")

if a == 0 and b == 0 and c == 0:
    print("Бесконечное множество решений.\n")
    exit()

d = b*b - 4 * a * c

if d < 0:
    print("Дискриминант: %s.\nЭто уравнение не имеет решений." %d)
    
elif a != 0: 
    x1 = ((-b + sqrt(d)) / (2*a))
    x2 = ((-b - sqrt(d)) / (2*a))
    
    if x1 >= 0 or x2 >= 0:
        print("Решение уравнения:")
        
    else:
        print("Это уравнение не имеет решений.")
    
    if x1 >= 0:
        x11 = sqrt(x1)
        x12 = -sqrt(x1)
        print("%s, %s" %(x11, x12))
        
    if x2 >= 0: 
        x21 = sqrt(x2)
        x22 = -sqrt(x2)
        print("%s, %s\n" %(x21, x22))

else:
    try:
        x11 = sqrt(-c/b)
        x12 = -sqrt(-c/b)
        print("Решение уравнения:\n%s, %s\n" %(x11, x12))
        
    except:
        print("Это уравнение не имеет решений.")