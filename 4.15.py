import math
print("УРАВНЕНИЕ: ах**2 + bx + c")
a=float(input("введите а "))
b=float(input("введите b "))
c=float(input("введите c "))
D=b**2-4*a*c
print("D=",D)
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("x1=",x1 , "x2=",x2)
elif D==0:
    x=-b/(2*a)
    print("x=",x)
else:
    print("Нет корней в уравнении")